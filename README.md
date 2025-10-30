# 141 Discussion — Interactive Python Practice Framework

> **IMPORTANT DISCLAIMER**
>
> I do not know what will be on the midterm. This guide may miss topics. You should study outside of this repo as well. I put in a good‑faith effort to cover as much as possible, but please don’t blame me if something is missing :(. I genuinely hope this is useful for your studying. If you have any feedback, comments, or concerns, just email me or come to my oh

## Overview
This repository provides a complete practice and testing environment to help students prepare for Python fundamentals and midterm-style programming questions.  
It covers expressions, conditionals, loops, strings, lists, tuples, lists of lists, scoping, mutability, copying, and more. Start with the assessment, then do the Extra Questions early — they are intentionally tricky and not always intuitive.

Each file in the `problems/` directory represents a category of problems, paired with corresponding:
- `tests/` → automated pytest-based test cases
- `solutions/` → reference implementations for checking results

---

## Repository Structure

```
.
├── problems/
│   ├── assessment.py          # Diagnostic problems across all topics
│   ├── expressions.py         # Arithmetic, logic, and computation
│   ├── conditional_loops.py   # Conditionals, iteration, and control flow
│   ├── strings_list.py        # String and list manipulation
│   ├── extra_qs.py            # Conceptual "Guess the Output" and theory drills
│   └── ...
├── solutions/
│   ├── assessment_sols.py
│   ├── expressions_sols.py
│   ├── conditional_loops_sols.py
│   ├── strings_list_sols.py
│   ├── extra_qs_sols.py
│   └── ...
├── tests/
│   ├── assessment_tests.py
│   ├── expressions_tests.py
│   ├── conditional_loops_tests.py
│   ├── strings_list_tests.py
│   ├── extra_qs_tests.py
│   └── ...
├── scripts/
│   └── drill_prompts.py       # Interactive “test mode” problem selector
└── README.md
```

---

## Where to Start

1) **Run the assessment** (`problems/assessment.py`) to gauge your baseline.
2) **Tackle Extra Questions early** (`problems/extra_qs.py`). These “guess the output” drills expose scope, mutability, copying, and truthiness pitfalls that aren’t intuitive. They will make the later coding problems easier.
3) Move on to the topic files (`expressions.py`, `conditional_loops.py`, `strings_list.py`), using tags and difficulty to focus your practice.

---

## Getting Started

### 0. Clone the Repository

```bash
git clone https://github.com/cmbenello/141-discussion.git
codium 141-discussion # This is whereever you saved it like just type codium file location and open it up
```

### 1. Create and Activate a Virtual Environment

Use Python 3.12 or later:

```bash
python3 -m venv venv
source venv/bin/activate  # (on macOS/Linux)
venv\Scripts\activate     # (on Windows)
```

### 2. Install Dependencies

Install requirements (pytest and any extras):

```bash
pip install -r requirements.txt
```

### 3. Run all tests

Run the full test suite to check every problem:

```bash
pytest -q
```

### 4. Run tests for one topic

```bash
pytest -q tests/expressions_tests.py
pytest -q tests/conditional_loops_tests.py
pytest -q tests/strings_list_tests.py
```

### 5. Run tests for one function

Use `-k` to target a single function:

```bash
pytest -q -k "expr_24_middle_three"
```

---

## Recommended Study Order

1. Assessment — quick self‑diagnosis (run this first).
2. Extra Questions — conceptual edge cases (do these early; they’re not intuitive).
3. Expressions — arithmetic and boolean logic.
4. Conditional Loops — `if`, `for`, `while`, and iteration patterns.
5. Strings & Lists — slicing, comprehension, transformations.

---

## Problem Categories

Each problem file focuses on a specific conceptual area:

| File | Topic | Focus |
|------|--------|--------|
| `assessment.py` | Mixed practice | Foundation review |
| `expressions.py` | Operators, math, logic | Arithmetic expressions, rounding, conditionals |
| `conditional_loops.py` | Flow control | `if`, `for`, `while`, range, iteration |
| `strings_list.py` | Sequence data | String parsing, slicing, comprehension, transformations |
| `extra_qs.py` | Conceptual reasoning (do these right after the assessment) | Scoping, mutability, copying, truthiness |

---

## Tags and Difficulty Levels

Each function starts with a detailed docstring including:
- Category: conceptual grouping (e.g. “String Algorithms”, “Numeric Iteration”)
- Tags: quick hints for the concepts required (e.g. `range`, `product`, `indexing`)
- Difficulty: estimated effort (1–4)
  - 1 — basic comprehension
  - 2 — simple reasoning or implementation
  - 3 — moderate complexity / multiple concepts combined
  - 4 — challenging multi-step logic

You can use these to focus on your weak areas.  
For example:

```python
def cl_02_product_multiples_range(a: int, b: int, k: int) -> int:
    """
    Category: Numeric Iteration & Accumulation | Tags: range, product, divisibility | Difficulty: 2
    """
```

---

## Extra Questions (Conceptual / “Guess the Output”)

The file `extra_qs.py` is different from the coding ones — you don’t write full programs here.  
Instead, you predict what the provided snippet would print and return that as data. They are high‑leverage practice because many bugs on exams come from these semantics.

Rules:
- Return what the snippet would print.
- If multiple lines, return a list of strings.
- If it raises an error, return `-1`.
- If it computes a value, return that value.

Example:

```python
def scope_01_shadowing():
    # x = 5
    # def f(): x = 10; print("inside:", x)
    # f(); print("outside:", x)
    return (10, 5)
```

---

## Solutions

Each file in `solutions/` mirrors the `problems/` layout.  
To activate solution mode:

```bash
export USE_SOLUTIONS=1
pytest -q tests/expressions_tests.py
```

This lets pytest check your solutions directly against the reference implementations.

If unset, tests will check your own implementations.

---

## Testing Reference

### To test one topic

```bash
pytest tests/strings_list_tests.py
```

### To test one specific function

```bash
pytest -q -k "sl_36_max_subarray_sum"
```

### To test all topics but show summary only

```bash
pytest -q --maxfail=1 --disable-warnings
```

---

## Interactive Drill Mode

The file `scripts/drill_prompts.py` provides a lightweight interactive quiz generator.

Run it to practice:

```bash
python scripts/drill_prompts.py
```

Flags:
- `--all` — list all available problems
- `--extra <n>` — number of extra conceptual questions (default: 6)
- `--per <n>` — number of normal problems per topic (default: 3)

---

## Tips

- Use docstrings and tags to identify which concepts you need.
- Don’t skip the Extra Questions — they help with understanding scope and Python semantics.
- Use `pytest -k` to test your understanding problem-by-problem.
- Solutions are provided for learning, not just checking — read the explanations carefully.

---

## Example Workflow

```bash
# 1. Practice a few problems manually
python scripts/drill_prompts.py --extra 4 --per 2

# 2. Edit your solution
codium problems/expressions.py

# 3. Test one file
pytest -q tests/expressions_tests.py

# 4. View official solution explanation
less solutions/expressions_sols.py
```

---

I am confident all of you will do great! (ㅇㅅㅇ)/

---

— ㅊ 다녀감
