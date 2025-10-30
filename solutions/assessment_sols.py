

from __future__ import annotations
from typing import Any, Iterable, List, Optional, Tuple
import math
import copy as _copy

# ==============================
# Module-level state for scoping
# ==============================
GLOBAL_COUNTER = 0

# ------------------------------
# 1) TYPES / EXPRESSIONS (5)
# ------------------------------

def expr_01_add_one_and_multiply(a: int, x: int) -> int:
    return (abs(a) + 1) * x


def expr_02_int_div_and_mod(a: int, b: int) -> Tuple[int, int]:
    return a // b, a % b


def expr_03_mean_of_three(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3.0


def expr_04_bool_combo(p: bool, q: bool, r: bool) -> bool:
    # A non-trivial combo; any equivalent boolean is fine
    return (p and not q) or r


def expr_05_clamp(val: int, lo: int, hi: int) -> int:
    if val < lo:
        return lo
    if val > hi:
        return hi
    return val

# ------------------------------
# 2) FUNCTIONS (5)
# ------------------------------

def func_01_sign(n: int) -> int:
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0


def func_02_apply_twice(f, x: Any) -> Any:
    return f(f(x))


def func_03_default_step_sum(n: int, step: int = 1) -> int:
    total = 0
    i = 0
    while i <= n:
        total += i
        i += step
    return total


def func_04_in_place_append(target: List[int], value: int) -> None:
    target.append(value)
    return None


def func_05_shadowing_demo(x: int) -> int:
    # Show that a local variable named x shadows the parameter
    y = x
    x = x + 1  # shadow and change locally
    return x - y  # always 1

# ------------------------------
# 3) CONDITIONALS (5)
# ------------------------------

def cond_01_is_even(n: int) -> bool:
    return n % 2 == 0


def cond_02_grade_bucket(score: int) -> str:
    # Typical cutoffs
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'


def cond_03_max_of_three(a: int, b: int, c: int) -> int:
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m


def cond_04_abs_val(n: int) -> int:
    if n < 0:
        return -n
    return n


def cond_05_triangle_type(a: int, b: int, c: int) -> Optional[str]:
    # Validate triangle inequality and positive lengths
    sides = sorted([a, b, c])
    if sides[0] <= 0 or sides[0] + sides[1] <= sides[2]:
        return None
    if a == b == c:
        return 'equilateral'
    if a == b or b == c or a == c:
        return 'isosceles'
    return 'scalene'

# ------------------------------
# 4) LOOPS (5)
# ------------------------------

def loop_01_factorial(n: int) -> int:
    result = 1
    i = 2
    while i <= n:
        result *= i
        i += 1
    return result


def loop_02_count_until(lst: List[int], stop_at: int) -> int:
    count = 0
    for v in lst:
        if v == stop_at:
            break
        count += 1
    return count


def loop_03_sum_first_k_multiples(k: int, m: int) -> int:
    total = 0
    i = 1
    while i <= k:
        total += i * m
        i += 1
    return total


def loop_04_first_index_of(lst: List[Any], target: Any) -> Optional[int]:
    for i, v in enumerate(lst):
        if v == target:
            return i
    return None


def loop_05_has_increasing_pair(lst: List[int]) -> bool:
    if len(lst) < 2:
        return False
    prev = lst[0]
    for v in lst[1:]:
        if prev < v:
            return True
        prev = v
    return False

# ------------------------------
# 5) STRINGS (5)
# ------------------------------

def str_01_count_vowels(s: str) -> int:
    vowels = set('aeiouAEIOU')
    return sum(1 for ch in s if ch in vowels)


def str_02_reverse_words(s: str) -> str:
    parts = [w for w in s.strip().split() if w]
    parts.reverse()
    return ' '.join(parts)


def str_03_toggle_case_ascii(s: str) -> str:
    out_chars = []
    for ch in s:
        code = ord(ch)
        if 65 <= code <= 90:        # A-Z
            out_chars.append(chr(code + 32))
        elif 97 <= code <= 122:     # a-z
            out_chars.append(chr(code - 32))
        else:
            out_chars.append(ch)
    return ''.join(out_chars)


def str_04_shift_digits_wrap(s: str, k: int) -> str:
    out = []
    k = k % 10
    for ch in s:
        if ch.isdigit():
            d = ord(ch) - ord('0')
            nd = (d + k) % 10
            out.append(chr(nd + ord('0')))
        else:
            out.append(ch)
    return ''.join(out)


def str_05_alpha_only(s: str) -> str:
    return ''.join(ch for ch in s if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'))

# ------------------------------
# 6) LISTS (5)
# ------------------------------

def list_01_sum(nums: List[int]) -> int:
    total = 0
    for v in nums:
        total += v
    return total


def list_02_min_index(nums: List[int]) -> Optional[int]:
    if not nums:
        return None
    m_idx = 0
    m_val = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < m_val:
            m_val = nums[i]
            m_idx = i
    return m_idx


def list_03_dedup_preserve_order(nums: List[int]) -> List[int]:
    seen = set()
    out: List[int] = []
    for v in nums:
        if v not in seen:
            seen.add(v)
            out.append(v)
    return out


def list_04_rotate_right(lst: List[Any], k: int) -> List[Any]:
    n = len(lst)
    if n == 0:
        return []
    k = k % n
    if k == 0:
        return lst.copy()
    return lst[-k:] + lst[:-k]


def list_05_all_prefix_sums(nums: List[int]) -> List[int]:
    out: List[int] = []
    running = 0
    for v in nums:
        running += v
        out.append(running)
    return out

# ------------------------------
# 7) TUPLES (5)
# ------------------------------

def tup_01_swap_ends(t: Tuple[Any, ...]) -> Tuple[Any, ...]:
    n = len(t)
    if n < 2:
        return t
    return (t[-1],) + t[1:-1] + (t[0],)


def tup_02_pairwise_sum(a: Tuple[int, ...], b: Tuple[int, ...]) -> Tuple[int, ...]:
    n = min(len(a), len(b))
    return tuple(a[i] + b[i] for i in range(n))


def tup_03_contains_all(t: Tuple[Any, ...], items: Iterable[Any]) -> bool:
    s = set(t)
    for it in items:
        if it not in s:
            return False
    return True


def tup_04_middle_slice(t: Tuple[Any, ...], start: int, end: int) -> Tuple[Any, ...]:
    return t[start:end]


def tup_05_unpack_head_tail(t: Tuple[Any, ...]) -> Tuple[Optional[Any], Tuple[Any, ...], Optional[Any]]:
    if not t:
        return None, (), None
    if len(t) == 1:
        return t[0], (), None
    return t[0], t[1:-1], t[-1]

# ------------------------------
# 8) LISTS OF LISTS / TABLES (5)
# ------------------------------

def lol_01_flatten(lst2d: List[List[Any]]) -> List[Any]:
    out: List[Any] = []
    for row in lst2d:
        for v in row:
            out.append(v)
    return out


def lol_02_row_means(table: List[List[float]]) -> List[float]:
    means: List[float] = []
    for row in table:
        s = 0.0
        for v in row:
            s += v
        means.append(s / len(row))
    return means


def lol_03_extract_column(table: List[List[Any]], col_idx: int) -> List[Any]:
    out: List[Any] = []
    # Always skip header row:
    for r in range(1, len(table)):
        row = table[r]
        if col_idx < len(row):
            out.append(row[col_idx])
    return out


def lol_04_select_columns(table: List[List[Any]], indices: List[int]) -> List[List[Any]]:
    if not table:
        return []
    out = []
    # header
    out.append([table[0][i] for i in indices])
    # rows
    for row in table[1:]:
        out.append([row[i] for i in indices])
    return out


def lol_05_filter_rows_eq(table: List[List[Any]], col_idx: int, value: Any) -> List[List[Any]]:
    if not table:
        return []
    out = [table[0]]  # keep header if present
    for row in table[1:]:
        if col_idx < len(row) and row[col_idx] == value:
            out.append(row)
    # If there was no header (single row), handle generically
    if len(table) == 1 and table[0]:
        return [r for r in table if r[col_idx] == value]
    return out

# ------------------------------
# 9) FUNCTION SCOPING (5)
# ------------------------------

def scope_01_local_vs_global(x: int) -> Tuple[int, int]:
    # Demonstrate local x separate from GLOBAL_COUNTER
    local_x = x + 1
    return local_x, GLOBAL_COUNTER


def scope_02_counter_increment(times: int) -> int:
    global GLOBAL_COUNTER
    for _ in range(times):
        GLOBAL_COUNTER += 1
    return GLOBAL_COUNTER


def scope_03_inner_function_capture(start: int) -> int:
    base = start

    def inner() -> int:
        return base + 1

    return inner()


def scope_04_parameter_shadowing(x: int) -> int:
    # There might be an outer x; this parameter shadows it.
    return x + 2


def scope_05_mutable_param_side_effect(acc: List[int], n: int) -> None:
    for i in range(n):
        acc.append(i)
    return None

# ------------------------------
# 10) PASS-BY & COPY SEMANTICS (5)
# ------------------------------

def copy_01_identity_vs_equality(a: Any, b: Any) -> Tuple[bool, bool]:
    return (a is b, a == b)


def copy_02_shallow_copy_list(x: List[List[int]]) -> Tuple[List[List[int]], List[List[int]]]:
    shallow = [row for row in x]  # list() would also work
    deep = _copy.deepcopy(x)
    return shallow, deep


def copy_03_append_vs_rebind(lst: List[int]) -> Tuple[List[int], List[int]]:
    after_append = lst.copy()
    after_append.append(99)          # e.g., [1, 2, 99]
    after_rebind = lst.copy() + [100]  # e.g., [1, 2, 100]  (different from after_append)
    return after_append, after_rebind


def copy_04_inplace_vs_outofplace_sort(lst: List[int]) -> Tuple[List[int], List[int]]:
    inplace_sorted = lst.copy()
    inplace_sorted.sort()
    outofplace_sorted = sorted(lst)
    return inplace_sorted, outofplace_sorted


def copy_05_aliasing_demo(lst: List[int]) -> Tuple[List[int], List[int]]:
    y = lst
    return lst, y


__all__ = [name for name in globals().keys() if not name.startswith('_')]