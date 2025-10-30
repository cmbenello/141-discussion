# problems/assessement.py
# Midterm assessment scaffold: 10 topics × 5 problems each (50 total).
# Prompts are intentionally concise ("exam/leetcode" vibe).
# Implementations should be written by students; for now each raises ValueError.

from __future__ import annotations
from typing import List, Tuple, Optional, Iterable, Any, Dict


# -------------------------
# Topic registry (metadata)
# -------------------------
TOPICS: Dict[str, str] = {}  # filled by _tag decorator below


def _tag(topic: str):
    """Decorator to record the topic category for each problem."""
    def deco(fn):
        TOPICS[fn.__name__] = topic
        return fn
    return deco


# =========================
# 1) TYPES / EXPRESSIONS
# =========================

@_tag("expressions")
def expr_01_add_one_and_multiply(a: int, x: int) -> int:
    """
    Increase `a` by 1, then combine with `x` via multiplication. Return the result.

    Args:
        a (int): base integer to be incremented
        x (int): multiplier

    Returns:
        int: the computed integer result

    Examples:
        >>> expr_01_add_one_and_multiply(5, 2)
        12
        >>> expr_01_add_one_and_multiply(9, -2)
        -20
    """
    raise ValueError("todo: expr_01_add_one_and_multiply")


@_tag("expressions")
def expr_02_int_div_and_mod(a: int, b: int) -> Tuple[int, int]:
    """
    Return (q, r) where q is floor-division of a by b and r is remainder. Assume b != 0.

    Args:
        a (int): dividend
        b (int): nonzero divisor

    Returns:
        Tuple[int, int]: (a // b, a % b)

    Examples:
        >>> expr_02_int_div_and_mod(7, 3)
        (2, 1)
        >>> expr_02_int_div_and_mod(-7, 3)
        (-3, 2)
    """
    raise ValueError("todo: expr_02_int_div_and_mod")


@_tag("expressions")
def expr_03_mean_of_three(a: float, b: float, c: float) -> float:
    """
    Return the arithmetic mean of three numbers as float.

    Args:
        a (float): first value
        b (float): second value
        c (float): third value

    Returns:
        float: mean of a, b, c

    Examples:
        >>> expr_03_mean_of_three(1.0, 2.0, 4.0)
        2.3333333333333335
        >>> expr_03_mean_of_three(0.0, 0.0, 0.0)
        0.0
    """
    raise ValueError("todo: expr_03_mean_of_three")


@_tag("expressions")
def expr_04_bool_combo(p: bool, q: bool, r: bool) -> bool:
    """
    Compute a Boolean expression combining p, q, r (document your chosen logic in code).

    Args:
        p (bool): flag
        q (bool): flag
        r (bool): flag

    Returns:
        bool: result of the chosen boolean combination

    Examples:
        >>> isinstance(expr_04_bool_combo(True, False, True), bool)
        True
    """
    raise ValueError("todo: expr_04_bool_combo")


@_tag("expressions")
def expr_05_clamp(val: int, lo: int, hi: int) -> int:
    """
    Return `val` constrained to the inclusive range [lo, hi]. Assume lo <= hi.

    Args:
        val (int): value to clamp
        lo (int): lower bound
        hi (int): upper bound

    Returns:
        int: clamped value

    Examples:
        >>> expr_05_clamp(10, 0, 5)
        5
        >>> expr_05_clamp(-2, -1, 3)
        -1
    """
    raise ValueError("todo: expr_05_clamp")


# =========================
# 2) FUNCTIONS
# =========================

@_tag("functions")
def func_01_sign(n: int) -> int:
    """
    Return -1, 0, or 1 depending on sign of n.

    Args:
        n (int): integer

    Returns:
        int: -1 if n &lt; 0, 0 if n == 0, 1 if n &gt; 0

    Examples:
        >>> func_01_sign(-8)
        -1
        >>> func_01_sign(0)
        0
    """
    raise ValueError("todo: func_01_sign")


@_tag("functions")
def func_02_apply_twice(f, x: Any) -> Any:
    """
    Call f(f(x)) and return the result.

    Args:
        f (callable): unary function
        x (Any): input

    Returns:
        Any: f(f(x))

    Examples:
        >>> func_02_apply_twice(lambda y: y + 1, 3)
        5
        >>> func_02_apply_twice(str, 7)
        '7'
    """
    raise ValueError("todo: func_02_apply_twice")


@_tag("functions")
def func_03_default_step_sum(n: int, step: int = 1) -> int:
    """
    Sum 0..n inclusive with the given step. Assume n &gt;= 0 and step &gt; 0.

    Args:
        n (int): upper bound (inclusive)
        step (int): positive step size (default 1)

    Returns:
        int: arithmetic sum of the sequence

    Examples:
        >>> func_03_default_step_sum(5)
        15
        >>> func_03_default_step_sum(6, step=2)
        12
    """
    raise ValueError("todo: func_03_default_step_sum")


@_tag("functions")
def func_04_in_place_append(target: List[int], value: int) -> None:
    """
    Append value to target in place. Do not return anything.

    Args:
        target (List[int]): list to mutate
        value (int): value to append

    Returns:
        None

    Examples:
        >>> data = [1, 2]
        >>> _ = func_04_in_place_append(data, 3)
        >>> data
        [1, 2, 3]
    """
    raise ValueError("todo: func_04_in_place_append")


@_tag("functions")
def func_05_shadowing_demo(x: int) -> int:
    """
    Return a value that distinguishes local vs parameter shadowing (write minimal example).

    Args:
        x (int): input

    Returns:
        int: value showing shadowing behavior

    Examples:
        >>> isinstance(func_05_shadowing_demo(10), int)
        True
    """
    raise ValueError("todo: func_05_shadowing_demo")


# =========================
# 3) CONDITIONALS
# =========================

@_tag("conditionals")
def cond_01_is_even(n: int) -> bool:
    """
    Return True iff n is divisible by 2.

    Args:
        n (int): integer

    Returns:
        bool: parity test

    Examples:
        >>> cond_01_is_even(8)
        True
        >>> cond_01_is_even(7)
        False
    """
    raise ValueError("todo: cond_01_is_even")


@_tag("conditionals")
def cond_02_grade_bucket(score: int) -> str:
    """
    Return letter grade 'A'..'F' based on integer score 0..100 (choose sane cutoffs).

    Args:
        score (int): 0..100

    Returns:
        str: single uppercase letter

    Examples:
        >>> cond_02_grade_bucket(95) in {'A','B','C','D','F'}
        True
    """
    raise ValueError("todo: cond_02_grade_bucket")


@_tag("conditionals")
def cond_03_max_of_three(a: int, b: int, c: int) -> int:
    """
    Return the largest of the three integers (ties allowed).

    Args:
        a (int): first
        b (int): second
        c (int): third

    Returns:
        int: maximum

    Examples:
        >>> cond_03_max_of_three(3, 9, 5)
        9
    """
    raise ValueError("todo: cond_03_max_of_three")


@_tag("conditionals")
def cond_04_abs_val(n: int) -> int:
    """
    Return absolute value of n without using built-ins that compute abs directly.

    Args:
        n (int): integer

    Returns:
        int: |n|

    Examples:
        >>> cond_04_abs_val(-7)
        7
        >>> cond_04_abs_val(0)
        0
    """
    raise ValueError("todo: cond_04_abs_val")


@_tag("conditionals")
def cond_05_triangle_type(a: int, b: int, c: int) -> Optional[str]:
    """
    Given side lengths, return 'equilateral'/'isosceles'/'scalene' or None if invalid.

    Args:
        a (int): side
        b (int): side
        c (int): side

    Returns:
        Optional[str]: triangle class or None

    Examples:
        >>> cond_05_triangle_type(3, 3, 3)
        'equilateral'
        >>> cond_05_triangle_type(2, 3, 5) is None
        True
    """
    raise ValueError("todo: cond_05_triangle_type")


# =========================
# 4) LOOPS
# =========================

@_tag("loops")
def loop_01_factorial(n: int) -> int:
    """
    Return n! for n &gt;= 0 using a loop.

    Args:
        n (int): nonnegative integer

    Returns:
        int: factorial

    Examples:
        >>> loop_01_factorial(5)
        120
        >>> loop_01_factorial(0)
        1
    """
    raise ValueError("todo: loop_01_factorial")


@_tag("loops")
def loop_02_count_until(lst: List[int], stop_at: int) -> int:
    """
    Iterate lst left-to-right; return count of elements seen before first stop_at. If absent, return len(lst).

    Args:
        lst (List[int]): numbers
        stop_at (int): sentinel

    Returns:
        int: count before first stop_at

    Examples:
        >>> loop_02_count_until([1,2,3,2], 2)
        1
        >>> loop_02_count_until([9,9,9], 5)
        3
    """
    raise ValueError("todo: loop_02_count_until")


@_tag("loops")
def loop_03_sum_first_k_multiples(k: int, m: int) -> int:
    """
    Sum the first k positive multiples of m (k &gt;= 0).

    Args:
        k (int): how many multiples
        m (int): base

    Returns:
        int: sum of m + 2m + ... + k*m (0 if k==0)

    Examples:
        >>> loop_03_sum_first_k_multiples(3, 4)
        24
        >>> loop_03_sum_first_k_multiples(0, 7)
        0
    """
    raise ValueError("todo: loop_03_sum_first_k_multiples")


@_tag("loops")
def loop_04_first_index_of(lst: List[Any], target: Any) -> Optional[int]:
    """
    Return first index of target in lst, or None if not present. Short-circuit appropriately.

    Args:
        lst (List[Any]): sequence
        target (Any): value

    Returns:
        Optional[int]: index or None

    Examples:
        >>> loop_04_first_index_of(['a','b','c'], 'b')
        1
        >>> loop_04_first_index_of([], 42) is None
        True
    """
    raise ValueError("todo: loop_04_first_index_of")


@_tag("loops")
def loop_05_has_increasing_pair(lst: List[int]) -> bool:
    """
    Return True iff there exists i with lst[i] &lt; lst[i+1].

    Args:
        lst (List[int]): numbers

    Returns:
        bool: whether any adjacent increase exists

    Examples:
        >>> loop_05_has_increasing_pair([3,2,1])
        False
        >>> loop_05_has_increasing_pair([1,1,2])
        True
    """
    raise ValueError("todo: loop_05_has_increasing_pair")


# =========================
# 5) STRINGS
# =========================

@_tag("strings")
def str_01_count_vowels(s: str) -> int:
    """
    Count vowels a/e/i/o/u in either case (do not count 'y').

    Args:
        s (str): text

    Returns:
        int: number of vowels

    Examples:
        >>> str_01_count_vowels('University of Chicago')
        10
        >>> str_01_count_vowels('rhythm')
        0
    """
    raise ValueError("todo: str_01_count_vowels")


@_tag("strings")
def str_02_reverse_words(s: str) -> str:
    """
    Return words of s in reverse order; single-space separated; trimmed.

    Args:
        s (str): sentence

    Returns:
        str: reversed word order

    Examples:
        >>> str_02_reverse_words('  a  b   c ')
        'c b a'
        >>> str_02_reverse_words('hello')
        'hello'
    """
    raise ValueError("todo: str_02_reverse_words")


@_tag("strings")
def str_03_toggle_case_ascii(s: str) -> str:
    """
    Toggle case for A–Z/a–z via ASCII arithmetic; leave others unchanged.

    Args:
        s (str): text

    Returns:
        str: toggled

    Examples:
        >>> str_03_toggle_case_ascii('GoodPassword')
        'gOODpASSWORD'
        >>> str_03_toggle_case_ascii('MoNkEy123')
        'mOnKeY123'
    """
    raise ValueError("todo: str_03_toggle_case_ascii")


@_tag("strings")
def str_04_shift_digits_wrap(s: str, k: int) -> str:
    """
    Shift every digit by k modulo 10; non-digits unchanged; -9 &lt;= k &lt;= 9.

    Args:
        s (str): text
        k (int): shift

    Returns:
        str: shifted digits

    Examples:
        >>> str_04_shift_digits_wrap('123456', 3)
        '456789'
        >>> str_04_shift_digits_wrap('0abc9', -1)
        '9abc8'
    """
    raise ValueError("todo: str_04_shift_digits_wrap")


@_tag("strings")
def str_05_alpha_only(s: str) -> str:
    """
    Return s with all non-alphabetic characters removed (A–Z and a–z only).

    Args:
        s (str): text

    Returns:
        str: letters only

    Examples:
        >>> str_05_alpha_only('ladyGAGA25!')
        'ladyGAGA'
        >>> str_05_alpha_only('qwerty')
        'qwerty'
    """
    raise ValueError("todo: str_05_alpha_only")


# =========================
# 6) LISTS
# =========================

@_tag("lists")
def list_01_sum(nums: List[int]) -> int:
    """
    Return the sum of nums without mutating the input.

    Args:
        nums (List[int]): numbers

    Returns:
        int: total

    Examples:
        >>> lst = [1,2,3]
        >>> list_01_sum(lst)
        6
        >>> lst
        [1, 2, 3]
    """
    raise ValueError("todo: list_01_sum")


@_tag("lists")
def list_02_min_index(nums: List[int]) -> Optional[int]:
    """
    Return index of first minimum in nums; None if empty.

    Args:
        nums (List[int]): numbers

    Returns:
        Optional[int]: index or None

    Examples:
        >>> list_02_min_index([5,4,3,2,1])
        4
        >>> list_02_min_index([])
        None
    """
    raise ValueError("todo: list_02_min_index")


@_tag("lists")
def list_03_dedup_preserve_order(nums: List[int]) -> List[int]:
    """
    Return a new list with first occurrences only, preserving order.

    Args:
        nums (List[int]): numbers

    Returns:
        List[int]: de-duplicated in original order

    Examples:
        >>> list_03_dedup_preserve_order([1,2,1,3,2,4])
        [1, 2, 3, 4]
    """
    raise ValueError("todo: list_03_dedup_preserve_order")


@_tag("lists")
def list_04_rotate_right(lst: List[Any], k: int) -> List[Any]:
    """
    Return a new list rotated right by k (k may exceed length).

    Args:
        lst (List[Any]): items
        k (int): rotation amount

    Returns:
        List[Any]: rotated copy

    Examples:
        >>> list_04_rotate_right([1,2,3,4], 1)
        [4, 1, 2, 3]
        >>> list_04_rotate_right([1,2,3,4], 6)
        [3, 4, 1, 2]
    """
    raise ValueError("todo: list_04_rotate_right")


@_tag("lists")
def list_05_all_prefix_sums(nums: List[int]) -> List[int]:
    """
    Return list of prefix sums: [x0, x0+x1, ..., total].

    Args:
        nums (List[int]): numbers

    Returns:
        List[int]: prefix totals

    Examples:
        >>> list_05_all_prefix_sums([1,2,3])
        [1, 3, 6]
        >>> list_05_all_prefix_sums([])
        []
    """
    raise ValueError("todo: list_05_all_prefix_sums")


# =========================
# 7) TUPLES
# =========================

@_tag("tuples")
def tup_01_swap_ends(t: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """
    Return new tuple with first and last swapped (unchanged if len&lt;2).

    Args:
        t (Tuple[Any, ...]): input

    Returns:
        Tuple[Any, ...]: swapped or original

    Examples:
        >>> tup_01_swap_ends((1,2,3,4))
        (4, 2, 3, 1)
        >>> tup_01_swap_ends((1,))
        (1,)
    """
    raise ValueError("todo: tup_01_swap_ends")


@_tag("tuples")
def tup_02_pairwise_sum(a: Tuple[int, ...], b: Tuple[int, ...]) -> Tuple[int, ...]:
    """
    Return elementwise sums up to min length; ignore extras.

    Args:
        a (Tuple[int, ...]): first
        b (Tuple[int, ...]): second

    Returns:
        Tuple[int, ...]: pairwise sums

    Examples:
        >>> tup_02_pairwise_sum((1,2,3), (10,20))
        (11, 22)
    """
    raise ValueError("todo: tup_02_pairwise_sum")


@_tag("tuples")
def tup_03_contains_all(t: Tuple[Any, ...], items: Iterable[Any]) -> bool:
    """
    Return True iff every item in `items` appears in tuple t.

    Args:
        t (Tuple[Any, ...]): haystack
        items (Iterable[Any]): needles

    Returns:
        bool: containment test

    Examples:
        >>> tup_03_contains_all((1,2,3), [2,3])
        True
        >>> tup_03_contains_all((1,2,3), [4])
        False
    """
    raise ValueError("todo: tup_03_contains_all")


@_tag("tuples")
def tup_04_middle_slice(t: Tuple[Any, ...], start: int, end: int) -> Tuple[Any, ...]:
    """
    Return subtuple t[start:end] with Python slicing semantics.

    Args:
        t (Tuple[Any, ...]): source
        start (int): start index
        end (int): end index

    Returns:
        Tuple[Any, ...]: slice

    Examples:
        >>> tup_04_middle_slice((0,1,2,3,4), 1, 4)
        (1, 2, 3)
    """
    raise ValueError("todo: tup_04_middle_slice")


@_tag("tuples")
def tup_05_unpack_head_tail(t: Tuple[Any, ...]) -> Tuple[Optional[Any], Tuple[Any, ...], Optional[Any]]:
    """
    Return (head, middle, tail) where middle is the in-between subtuple.

    Args:
        t (Tuple[Any, ...]): tuple

    Returns:
        Tuple[Optional[Any], Tuple[Any, ...], Optional[Any]]: (head, middle, tail)

    Examples:
        >>> tup_05_unpack_head_tail((1,2,3,4))
        (1, (2, 3), 4)
        >>> tup_05_unpack_head_tail(())
        (None, (), None)
    """
    raise ValueError("todo: tup_05_unpack_head_tail")


# =========================
# 8) LISTS OF LISTS (TABLES)
# =========================

@_tag("lists_of_lists")
def lol_01_flatten(lst2d: List[List[Any]]) -> List[Any]:
    """
    Flatten a 2D list row-major into a new 1D list.

    Args:
        lst2d (List[List[Any]]): rows

    Returns:
        List[Any]: flattened

    Examples:
        >>> lol_01_flatten([[1,2],[3],[4,5]])
        [1, 2, 3, 4, 5]
    """
    raise ValueError("todo: lol_01_flatten")


@_tag("lists_of_lists")
def lol_02_row_means(table: List[List[float]]) -> List[float]:
    """
    Return arithmetic mean of each non-empty numeric row; do not mutate.

    Args:
        table (List[List[float]]): rows

    Returns:
        List[float]: row means

    Examples:
        >>> lol_02_row_means([[1,2,3],[4,5,6]])
        [2.0, 5.0]
    """
    raise ValueError("todo: lol_02_row_means")


@_tag("lists_of_lists")
def lol_03_extract_column(table: List[List[Any]], col_idx: int) -> List[Any]:
    """
    Return a list of the col_idx-th value from each row (skip header if present).

    Args:
        table (List[List[Any]]): table
        col_idx (int): column index

    Returns:
        List[Any]: column values

    Examples:
        >>> lol_03_extract_column([['a','b'], [1,2], [3,4]], 1)
        [2, 4]
    """
    raise ValueError("todo: lol_03_extract_column")


@_tag("lists_of_lists")
def lol_04_select_columns(table: List[List[Any]], indices: List[int]) -> List[List[Any]]:
    """
    Return a new table containing only the specified column indices, in order.

    Args:
        table (List[List[Any]]): table
        indices (List[int]): column indices

    Returns:
        List[List[Any]]: projected table

    Examples:
        >>> lol_04_select_columns([['a','b','c'], [1,2,3], [4,5,6]], [2,0])
        [['c', 'a'], [3, 1], [6, 4]]
    """
    raise ValueError("todo: lol_04_select_columns")


@_tag("lists_of_lists")
def lol_05_filter_rows_eq(table: List[List[Any]], col_idx: int, value: Any) -> List[List[Any]]:
    """
    Return rows whose col_idx equals value; include header if present.

    Args:
        table (List[List[Any]]): table
        col_idx (int): column index
        value (Any): match value

    Returns:
        List[List[Any]]: filtered rows (header first if present)

    Examples:
        >>> lol_05_filter_rows_eq([['x','y'], [1,2], [3,2]], 1, 2)
        [['x', 'y'], [1, 2], [3, 2]]
    """
    raise ValueError("todo: lol_05_filter_rows_eq")


# =========================
# 9) FUNCTION SCOPING
# =========================

GLOBAL_COUNTER = 0  # used by scope problems; students may read/modify intentionally


@_tag("scoping")
def scope_01_local_vs_global(x: int) -> Tuple[int, int]:
    """
    Demonstrate effect of assigning to a name also present at module level.
    Return (local_x, module_GLOBAL_COUNTER) after your logic.

    Args:
        x (int): input

    Returns:
        Tuple[int, int]: (local_x, GLOBAL_COUNTER)

    Examples:
        >>> isinstance(scope_01_local_vs_global(5), tuple)
        True
    """
    raise ValueError("todo: scope_01_local_vs_global")


@_tag("scoping")
def scope_02_counter_increment(times: int) -> int:
    """
    Increment a module-level counter `GLOBAL_COUNTER` `times` times and return its value.

    Args:
        times (int): nonnegative

    Returns:
        int: new GLOBAL_COUNTER value

    Examples:
        >>> isinstance(scope_02_counter_increment(2), int)
        True
    """
    raise ValueError("todo: scope_02_counter_increment")


@_tag("scoping")
def scope_03_inner_function_capture(start: int) -> int:
    """
    Create an inner function that references an outer-scope variable; return inner result.

    Args:
        start (int): seed

    Returns:
        int: value from inner function

    Examples:
        >>> isinstance(scope_03_inner_function_capture(10), int)
        True
    """
    raise ValueError("todo: scope_03_inner_function_capture")


@_tag("scoping")
def scope_04_parameter_shadowing(x: int) -> int:
    """
    Return a value showing parameter shadowing vs a same-named outer variable.

    Args:
        x (int): input

    Returns:
        int: demonstration value

    Examples:
        >>> isinstance(scope_04_parameter_shadowing(3), int)
        True
    """
    raise ValueError("todo: scope_04_parameter_shadowing")


@_tag("scoping")
def scope_05_mutable_param_side_effect(acc: List[int], n: int) -> None:
    """
    Illustrate side effects on a passed-in list by appending values 0..n-1.

    Args:
        acc (List[int]): accumulator (mutated)
        n (int): count

    Returns:
        None

    Examples:
        >>> acc = []
        >>> _ = scope_05_mutable_param_side_effect(acc, 3)
        >>> acc
        [0, 1, 2]
    """
    raise ValueError("todo: scope_05_mutable_param_side_effect")


# =========================
# 10) PASS-BY (MUTABILITY) & COPY SEMANTICS
# =========================

@_tag("copy_semantics")
def copy_01_identity_vs_equality(a: Any, b: Any) -> Tuple[bool, bool]:
    """
    Return (a_is_b, a_eq_b) using Python's identity and equality semantics.

    Args:
        a (Any): first
        b (Any): second

    Returns:
        Tuple[bool, bool]: (a is b, a == b)

    Examples:
        >>> copy_01_identity_vs_equality([1], [1])
        (False, True)
    """
    raise ValueError("todo: copy_01_identity_vs_equality")


@_tag("copy_semantics")
def copy_02_shallow_copy_list(x: List[List[int]]) -> Tuple[List[List[int]], List[List[int]]]:
    """
    Create a shallow copy of x and a deep copy of x; return (shallow, deep).
    Intended for later tests that mutate inner lists.

    Args:
        x (List[List[int]]): nested list

    Returns:
        Tuple[List[List[int]], List[List[int]]]: (shallow, deep)

    Examples:
        >>> sh, dp = copy_02_shallow_copy_list([[1],[2]])
        >>> (sh is dp, sh == dp)
        (False, True)
    """
    raise ValueError("todo: copy_02_shallow_copy_list")


@_tag("copy_semantics")
def copy_03_append_vs_rebind(lst: List[int]) -> Tuple[List[int], List[int]]:
    """
    Return two lists illustrating:
    - mutation via .append on the original,
    - rebinding to a new list (original unchanged).

    Args:
        lst (List[int]): base list

    Returns:
        Tuple[List[int], List[int]]: (after_append, after_rebind)

    Examples:
        >>> a, b = copy_03_append_vs_rebind([1,2])
        >>> a != b
        True
    """
    raise ValueError("todo: copy_03_append_vs_rebind")


@_tag("copy_semantics")
def copy_04_inplace_vs_outofplace_sort(lst: List[int]) -> Tuple[List[int], List[int]]:
    """
    Return (inplace_result, outofplace_result) to contrast list.sort() vs sorted(lst).
    Do not mutate the caller's list beyond what is required for the demonstration.

    Args:
        lst (List[int]): base list

    Returns:
        Tuple[List[int], List[int]]: (inplace_sorted, outofplace_sorted)

    Examples:
        >>> ins, outs = copy_04_inplace_vs_outofplace_sort([3,1,2])
        >>> ins == outs == [1,2,3]
        True
    """
    raise ValueError("todo: copy_04_inplace_vs_outofplace_sort")


@_tag("copy_semantics")
def copy_05_aliasing_demo(lst: List[int]) -> Tuple[List[int], List[int]]:
    """
    Create an alias y = lst; mutate via one name; return (lst, y) showing shared identity.

    Args:
        lst (List[int]): base list

    Returns:
        Tuple[List[int], List[int]]: (lst, alias)

    Examples:
        >>> a, b = copy_05_aliasing_demo([1,2])
        >>> a is b
        True
    """
    raise ValueError("todo: copy_05_aliasing_demo")