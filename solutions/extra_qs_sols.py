"""
Solutions for problems/extra_qs.py

IMPORTANT NOTE FOR GRADERS/READERS
----------------------------------
These solutions are **different** from typical function implementations: each
function returns what the *prompted snippet would print*, per the return
conventions defined in the assignment. We also add a brief "Why" explanation in
each docstring to justify the answer (scope, mutability, evaluation order, etc.).

Return Conventions Recap:
- If multiple lines would print -> return a list[str] with those exact lines.
- If an error would be raised -> return -1.
- If a single value would be printed -> return that value directly (int/tuple/str/etc.).
- Do **not** actually print in these solutions.
"""

from __future__ import annotations

# ======================================================
# 1) Variable Scope & Namespaces — Guess the Output (x10)
# ======================================================

def scope_01_shadowing() -> tuple[int, int]:
    """Why: Local assignment creates a new local `x` (10) that shadows global `x` (5).
    inside prints 10; outside prints global 5.
    """
    return (10, 5)


def scope_02_unbound_local() -> int:
    """Why: Assigning `x` in `g()` makes `x` local; `print(x)` before assignment causes
    UnboundLocalError. Per spec, return -1 on error.
    """
    return -1


def scope_03_global_stmt() -> list[str]:
    """Why: `global x` rebinds module `x` to 99. First prints the set message, then
    module-level `x` is 99.
    """
    return ["set x to 99", "after: 99"]


def scope_04_nonlocal_chain() -> list[str]:
    """Why: `nonlocal x` in inner updates the enclosing `x` from 1 to 3; both prints see 3.
    """
    return ["inner: 3", "outer: 3"]


def scope_05_comp_scope() -> list[str]:
    """Why: In Python 3, comprehension variable `x` is local to the comprehension; outer
    `x` remains 100. `y` becomes [0, 1, 2].
    """
    return ["y: [0, 1, 2]", "x: 100"]


def scope_06_for_var_leaks() -> int:
    """Why: After `for k in range(2)`, the last bound value of `k` is 1 and remains bound.
    """
    return 1


def scope_07_del_name() -> list[str]:
    """Why: `del x` removes the *name* only; `y` still references the list. Then `'x' in locals()`
    is False.
    """
    return ["[1]", "False"]


def scope_08_default_capture_time() -> int:
    """Why: Default argument `x=y` captures `y` at definition time (10), not call time (20).
    """
    return 10


def scope_09_nested_shadowing() -> list[str]:
    """Why: Each scope has its own `x`: inner=3, outer=2, global=1; prints reflect each scope.
    """
    return ["inner: 3", "outer: 2", "global: 1"]


def scope_10_class_scope_lookup() -> list[str]:
    """Why: Class body executes at definition -> prints `class body X = 2`. In method,
    name `X` resolves to global (1), `self.X` is instance attr lookup -> finds class attr 2,
    and `C.X` is 2.
    """
    return ["class body X = 2", "1 2 2"]


# ======================================
# 2) Mutability & Immutability (x10)
# ======================================

def mut_01_list_vs_tuple() -> list[str]:
    """Why: Lists are mutable; tuples are immutable. lst becomes [1, 99, 3]; tup unchanged.
    """
    return ["[1, 99, 3]", "(1, 2, 3)"]


def mut_02_string_methods() -> list[str]:
    """Why: `str.upper()` returns a new string; original `s` unchanged.
    """
    return ["t: HELLO", "s: hello"]


def mut_03_aliasing() -> str:
    """Why: `b` aliases `a`; appending via `b` also changes `a`. `a is b` is True.
    """
    return "[1, 2, 3] [1, 2, 3] True"


def mut_04_tuple_with_list() -> str:
    """Why: Tuples are immutable, but their *contents* can be mutable; list inside changes.
    """
    return "(1, [2, 3, 4])"


def mut_05_frozenset_behavior() -> list[str]:
    """Why: Set is mutable; frozenset is immutable. After add, s sorts to [1,2,3]; fs remains [1,2].
    """
    return ["[1, 2, 3]", "[1, 2]"]


def mut_06_bytes_vs_bytearray() -> list[str]:
    """Why: Assigning to `bytes` raises TypeError (name printed); `bytearray` accepts mutation,
    and bytes(ba) then shows b"dbc" since 100 = 'd'.
    """
    return ["TypeError", "b'dbc'"]


def mut_07_dict_alias_mutation() -> str:
    """Why: `d2` aliases `d1`; mutation via `d2` appears in `d1`.
    """
    return "{'x': 1, 'y': 2}"


def mut_08_tuple_concat_new_obj() -> str:
    """Why: Tuple concatenation creates a new tuple; `is` comparison is False.
    """
    return "(1, 2) (1, 2, 3) False"


def mut_09_list_copy_method() -> str:
    """Why: list.copy() is shallow; nested list is shared; a and b both show [[1,9],[2]]; a is b -> False.
    """
    return "[[1, 9], [2]] [[1, 9], [2]] False"


def mut_10_str_replace_creates_new() -> list[str]:
    """Why: `str.replace` returns a new string; original unchanged.
    """
    return ["bonono", "banana"]


# ================================
# 3) Shallow vs Deep Copy (x10)
# ================================

def copy_01_shallow_top() -> list[str]:
    """Why: `copy.copy` copies the outer list, but sublists are shared; changing b[0][0] affects a.
    """
    return ["[[99, 2], [3, 4]]", "[[99, 2], [3, 4]]"]


def copy_02_deepcopy() -> list[str]:
    """Why: `copy.deepcopy` clones nested lists; modifying b doesn't affect a.
    """
    return ["[[1, 2], [3, 4]]", "[[99, 2], [3, 4]]"]


def copy_03_slice_copy() -> str:
    """Why: Slicing makes a shallow copy; nested list shared -> both show [[1,9],[2]]; a is b False.
    """
    return "[[1, 9], [2]] [[1, 9], [2]] False"


def copy_04_dict_copy_vs_update() -> str:
    """Why: dict.copy() shallow-copies; the list at 'x' is shared and thus reflects append in both.
    """
    return "{'x': [1, 2]} {'x': [1, 2]}"


def copy_05_nested_tuple_copy() -> str:
    """Why: deepcopy clones list inside tuple; t1 unchanged; t2 gets list [2,3].
    """
    return "(1, [2]) (1, [2, 3])"


def copy_06_set_copy_independent() -> str:
    """Why: set.copy makes an independent set; adding to s2 doesn't change s1.
    """
    return "[1, 2] [1, 2, 3]"


def copy_07_copy_module_copy_vs_deepcopy() -> str:
    """Why: copy.copy shares nested dict; mutating c1 also mutates d; deepcopy c2 stays with old value.
    """
    return "9 1"


def copy_08_tuple_of_lists_shallow() -> str:
    """Why: Shallow copy of tuple shares inner lists; append via t2 appears in t as well.
    """
    return "([1, 5], [2]) ([1, 5], [2])"


def copy_09_list_of_dicts_deepcopy() -> str:
    """Why: Deepcopy isolates dicts; changing M doesn't affect L.
    """
    return "[{'x': 1}, {'y': 2}] [{'x': 99}, {'y': 2}]"


def copy_10_nested_defaultdict_shallow() -> str:
    """Why: Shallow copy shares the underlying mapping values and default factory; both lists show [1,2].
    """
    return "[1, 2] [1, 2]"


# ============================================================
# 4) Pass-by-Object-Reference & Function Args — (x10)
# ============================================================

def pass_01_int_param() -> list[str]:
    """Why: Int is immutable; bump prints inside: 11; outside remains 10.
    """
    return ["inside: 11", "outside: 10"]


def pass_02_list_param_mutate() -> list[str]:
    """Why: Mutating the list parameter mutates caller's list; both show [1,2,3,4].
    """
    return ["inside: [1, 2, 3, 4]", "outside: [1, 2, 3, 4]"]


def pass_03_rebind_list_param() -> list[str]:
    """Why: Rebinding `lst` to a new list doesn't affect caller; inside shows [9]; outside original.
    """
    return ["inside: [9]", "outside: [1, 2]"]


def pass_04_defaults_eval_once() -> bool:
    """Why: Default captures `t0` at definition; later sleep doesn't change equality -> True.
    """
    return True


def pass_05_kwargs_binding() -> int:
    """Why: Keyword args bind by name; 4*3 = 12.
    """
    return 12


def pass_06_args_collect() -> str:
    """Why: *args packs positional arguments into a tuple.
    """
    return "(1, 2, 3)"


def pass_07_kwargs_collect() -> str:
    """Why: **kwargs packs keyword args into dict; sorted items show [('a',1), ('z',3)].
    """
    return "[('a', 1), ('z', 3)]"


def pass_08_args_kwargs_mix() -> str:
    """Why: a=1, b overridden to 2 via **kw, remaining kw -> [('x',9)].
    """
    return "1 2 [('x', 9)]"


def pass_09_mutable_default_pitfall() -> list[str]:
    """Why: Mutable default list `acc` persists across calls -> prints [1] then [1, 2].
    """
    return ["[1]", "[1, 2]"]


def pass_10_safe_default_pattern() -> list[str]:
    """Why: Using None sentinel creates a fresh list each call -> prints [1] then [2].
    """
    return ["[1]", "[2]"]


# =====================================
# 5) Loops, else & break — (x10)
# =====================================

def loop_01_else_no_break() -> list[str]:
    """Why: Loop completes (0,1,2) then else runs -> 'done'.
    """
    return ["0", "1", "2", "done"]


def loop_02_else_with_break() -> list[str]:
    """Why: Break at i==1 prevents else; prints 0 then 'break at 1'.
    """
    return ["0", "break at 1"]


def loop_03_nested_breaks() -> list[str]:
    """Why: `break` exits only inner loop each time; outer continues for every i.
    """
    return [
        "0 0",
        "break inner",
        "outer continues",
        "1 0",
        "break inner",
        "outer continues",
    ]


def loop_04_while_truthy() -> list[str]:
    """Why: While pops last elements 3,2,1 then prints empty list at end.
    """
    return ["3", "2", "1", "[]"]


def loop_05_for_iterable_snapshot() -> list[str]:
    """Why: Iteration over list uses index progression that ignores runtime append for current pass;
    prints 1,2,3 then the final list includes appended 4.
    """
    return ["1", "2", "3", "[1, 2, 3, 4]"]


def loop_06_range_rebind_inside() -> list[str]:
    """Why: Rebinding loop var doesn't affect iteration sequence; prints 0,1,2.
    """
    return ["0", "1", "2"]


def loop_07_continue_skips_else() -> list[str]:
    """Why: `continue` does not skip else; only `break` does. Output shows 0, 'continue at 1', 2, then 'done'.
    """
    return ["0", "continue at 1", "2", "done"]


def loop_08_break_in_while_else() -> list[str]:
    """Why: While prints 3, then at n==2 it breaks; else after while is skipped.
    """
    return ["3", "break!"]


def loop_09_iter_mutate_delete() -> list[str]:
    """Why: Deleting while advancing index skips elements: prints 0,2, then final list is [1,3].
    """
    return ["0", "2", "[1, 3]"]


def loop_10_enumerate_safe() -> list[str]:
    """Why: Iterating over a copy avoids issues; removal affects `a` but not the iteration over `a[:]`.
    """
    return ["0 10", "1 20", "2 30", "[10, 30]"]


# ===============================================
# 6) Conditionals & Truthiness & Short-Circuit (x10)
# ===============================================

def cond_01_and_or_order() -> list[str]:
    """Why: `0 and 5` -> 0; `0 or 7` -> 7. `1 and 0` -> 0; `0 or 2` -> 2.
    """
    return ["7", "2"]


def cond_02_chain_compare() -> list[str]:
    """Why: `peek(2)` runs once; prints 'peek 2' then the chained comparison 1<2<3 is True.
    """
    return ["peek 2", "True"]


def cond_03_truthiness_values() -> list[str]:
    """Why: bool("") -> False; bool([0]) -> True (non-empty list); bool([]) -> False.
    """
    return ["False", "True", "False"]


def cond_04_none_identity() -> str:
    """Why: All `None` singletons have same identity and equality -> `True True`.
    """
    return "True True"


def cond_05_bool_ops_return_operand() -> list[str]:
    """Why: `[] or [1]` returns first truthy -> [1]; `[0] and 42` returns last operand since left is truthy -> 42.
    """
    return ["[1]", "42"]


def cond_06_ternary_binding() -> str:
    """Why: Expression is equivalent to `('A' if a < b else ('B' if b < 0 else 'C'))` -> 'A'.
    """
    return "A"


def cond_07_in_operator_strings() -> str:
    """Why: 'ana' is a substring of 'banana' -> True; 'x' not in -> False.
    """
    return "True False"


def cond_08_any_all_shortcircuit() -> list[str]:
    """Why: Generator yields 0->False, 0->False, then 3->True; `any` short-circuits there.
    """
    return ["check 0", "check 0", "check 3", "True"]


def cond_09_bool_int_arithmetic() -> str:
    """Why: True==1, False==0; sum -> 2; True*5 -> 5.
    """
    return "2 5"


def cond_10_dict_key_truthiness() -> str:
    """Why: The empty string key exists in dict (`'' in d` True) but bool('') is False.
    """
    return "True False"
