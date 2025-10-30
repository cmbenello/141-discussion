#!/usr/bin/env python3
"""
Drill Prompt Generator

- By default, shows 3 random problems from extra_qs first,
  then 2 random from each of: expressions, strings_list, conditional_loops, tables.
- It prints only the "Prompt:" section of each function's docstring (if present).
- Deterministic if you set DRILL_SEED=<int>.

Usage:
  python scripts/drill_prompts.py
  DRILL_SEED=141 python scripts/drill_prompts.py
  python scripts/drill_prompts.py --all            # list ALL problems (ordered)
  python scripts/drill_prompts.py --extra 5 --per 3
"""

import os
import re
import sys
import argparse
import random
import importlib
import inspect
from typing import List, Tuple

from pathlib import Path
# --- Make repo root importable so `problems.*` modules resolve when running this script directly
SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[1]  # project root (one level above scripts/)
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

PAIRINGS = [
    ("problems.extra_qs",        ["scope_", "mut_", "copy_", "pass_", "loop_", "cond_"]),  # we pick from these prefixes
    ("problems.expressions",     None),
    ("problems.strings_list",    None),
    ("problems.conditional_loops", None),
    ("problems.tables",          None),
]

PROMPT_RE = re.compile(r"(^|\n)\s*Prompt:\s*(?P<prompt>(?:.|\n)*)", re.IGNORECASE)

def rng_from_env():
    seed_env = os.getenv("DRILL_SEED")
    if seed_env is None:
        return random.Random()
    try:
        seed = int(seed_env)
    except ValueError:
        seed = sum(ord(c) for c in seed_env)
    return random.Random(seed)

def import_opt(modpath):
    try:
        return importlib.import_module(modpath)
    except Exception:
        return None

def func_names_in_module(mod, prefixes: List[str] | None) -> List[str]:
    out = []
    for name, obj in vars(mod).items():
        if not callable(obj) or name.startswith("_"):
            continue
        if prefixes is not None:
            if not any(name.startswith(p) for p in prefixes):
                continue
        # we keep all callables; arguments don’t matter since we only print prompts
        out.append(name)
    return sorted(out)

def get_prompt_from_doc(fn) -> Tuple[str, str]:
    """Return (title, prompt_text). Title is the function name + first doc line; prompt is the 'Prompt:' block (or all docstring)."""
    name = fn.__name__
    doc = inspect.getdoc(fn) or ""
    lines = [l.strip() for l in doc.splitlines()]
    title = name
    if lines:
        # grab the first non-empty line as a short title hint
        for l in lines:
            if l:
                title = f"{name} — {l}"
                break

    # Try to extract the 'Prompt:' block
    m = PROMPT_RE.search(doc)
    if m:
        prompt = m.group("prompt").strip()
    else:
        prompt = doc.strip()

    return title, prompt

def choose(rng: random.Random, seq, k):
    seq = list(seq)
    rng.shuffle(seq)
    if k is None:
        return seq
    return seq[:max(0, min(k, len(seq)))]

def print_section(header: str):
    bar = "-" * len(header)
    print(f"\n{header}\n{bar}")

def main(default_extra=6, default_per=3):
    parser = argparse.ArgumentParser(description="Drill Prompt Generator")
    parser.add_argument("--extra", type=int, default=default_extra, help="How many from extra_qs (first)")
    parser.add_argument("--per", type=int, default=default_per, help="How many from each other module")
    parser.add_argument("--all", action="store_true", help="List ALL problems from ALL modules (ordered), ignore sampling")
    args = parser.parse_args()

    rng = rng_from_env()

    # Import modules
    loaded = []
    for modpath, prefixes in PAIRINGS:
        mod = import_opt(modpath)
        if not mod:
            continue
        names = func_names_in_module(mod, prefixes)
        if not names:
            continue
        loaded.append((modpath, mod, names))

    if not loaded:
        print("No problem modules found. Did you run from repo root?", file=sys.stderr)
        sys.exit(1)

    # Order: extra_qs first (if present), then others
    loaded.sort(key=lambda x: (0 if x[0].endswith("extra_qs") else 1, x[0]))

    # Build selections
    selections = []
    if args.all:
        for modpath, mod, names in loaded:
            for name in names:
                selections.append((modpath, name))
    else:
        # extra_qs first
        for modpath, mod, names in loaded:
            if modpath.endswith("extra_qs"):
                picks = choose(rng, names, args.extra)
                for n in picks:
                    selections.append((modpath, n))
                break
        # then others
        for modpath, mod, names in loaded:
            if modpath.endswith("extra_qs"):
                continue
            picks = choose(rng, names, args.per)
            for n in picks:
                selections.append((modpath, n))

    # Render
    print_section("Drill Mode — Prompts Only (do NOT print in your answers)")
    seed_note = os.getenv("DRILL_SEED")
    if seed_note:
        print(f"Seed: {seed_note}")
    print("Return rules recap: If code prints multiple lines, return a list[str]. If it raises, return -1. Otherwise return the computed value.\n")

    # Group by module for readability
    by_mod = {}
    for modpath, name in selections:
        by_mod.setdefault(modpath, []).append(name)

    idx = 1
    for modpath in [m for m,_,_ in loaded]:
        if modpath not in by_mod:
            continue
        print_section(modpath)
        mod = import_opt(modpath)
        for name in by_mod[modpath]:
            fn = getattr(mod, name)
            title, prompt = get_prompt_from_doc(fn)
            print(f"[{idx}] {title}")
            print(prompt.strip())
            print()
            idx += 1

if __name__ == "__main__":
    main()