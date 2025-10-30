"""
Solutions for problems/expressions.py

These mirror the kept, curated functions (Levels 2–6).
Each function name exactly matches the corresponding stub in problems/expressions.py.
"""

from __future__ import annotations
import math
from typing import Any, Iterable, List, Optional, Sequence, Tuple


# =====================================================================================
# LEVEL 2
# =====================================================================================

def expr_14_seconds_to_hms(total_seconds: int) -> Tuple[int, int, int]:
    h = total_seconds // 3600
    rem = total_seconds % 3600
    m = rem // 60
    s = rem % 60
    return (h, m, s)


def expr_15_wrap_clock_12(hour: int) -> int:
    # Map integers to the 1..12 cycle; 12 stays 12.
    return ((hour - 1) % 12) + 1


def expr_16_tax_bracket_flag(income: int) -> float:
    if income <= 999:
        return 0.30
    if income <= 1999:
        return 0.40
    return 0.45


def expr_17_abs_diff(a: int, b: int) -> int:
    return a - b if a >= b else b - a


def expr_18_min_of_three(a: int, b: int, c: int) -> int:
    # Avoid relying on built-in min for pedagogy
    m = a if a <= b else b
    return m if m <= c else c


def expr_20_round_down_to_multiple(n: int, m: int) -> int:
    # Works for positive m; Python's % has sign of divisor (m)
    return n - (n % m)


# =====================================================================================
# LEVEL 3
# =====================================================================================

def expr_21_digit_sum(n: int) -> int:
    n = abs(n)
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def expr_24_middle_three(s: str) -> str:
    if len(s) < 3:
        raise ValueError("string must have length >= 3")
    mid = len(s) // 2
    return s[mid - 1: mid + 2]


def expr_25_ascii_shift_digit(s: str, k: int) -> str:
    out = []
    k_mod = k % 10
    for ch in s:
        if "0" <= ch <= "9":
            d = (ord(ch) - ord("0") + k_mod) % 10
            out.append(chr(ord("0") + d))
        else:
            out.append(ch)
    return "".join(out)


def expr_26_toggle_ascii_case(s: str) -> str:
    out = []
    for ch in s:
        if "a" <= ch <= "z":
            out.append(chr(ord(ch) - 32))
        elif "A" <= ch <= "Z":
            out.append(chr(ord(ch) + 32))
        else:
            out.append(ch)
    return "".join(out)


def expr_29_head_tail(xs: Sequence[Any]) -> Tuple[Optional[Any], Optional[Any]]:
    if not xs:
        return (None, None)
    first = xs[0]
    last = xs[-1]
    return (first, last)


# =====================================================================================
# LEVEL 4
# =====================================================================================

def expr_31_exactly_one_true(p: bool, q: bool, r: bool) -> bool:
    return (1 if p else 0) + (1 if q else 0) + (1 if r else 0) == 1


def expr_32_at_least_two_true(p: bool, q: bool, r: bool) -> bool:
    return (1 if p else 0) + (1 if q else 0) + (1 if r else 0) >= 2


def expr_33_safe_divide(a: int | float, b: int | float) -> Optional[float]:
    if b == 0:
        return None
    return a / b


def expr_34_between_inclusive(x: int | float, lo: int | float, hi: int | float) -> bool:
    return lo <= x <= hi


def expr_35_same_sign(x: int, y: int) -> bool:
    # Treat zero as neither positive nor negative
    return (x > 0 and y > 0) or (x < 0 and y < 0)


def expr_36_majority_parity_even(nums: Sequence[int]) -> bool:
    evens = sum(1 for v in nums if v % 2 == 0)
    odds = len(nums) - evens
    # Tie counts as even-majority per tests
    return evens >= odds


def expr_37_ends_with_vowel(s: str) -> bool:
    if not s:
        return False
    return s[-1] in "aeiouAEIOU"


def expr_38_is_palindrome_ignoring_case(s: str) -> bool:
    t = s.lower()
    return t == t[::-1]


def expr_39_safe_index(xs: Sequence[Any], idx: int) -> Optional[Any]:
    if 0 <= idx < len(xs):
        return xs[idx]
    return None


def expr_40_middle_of_three_sorted(a: int, b: int, c: int) -> int:
    # Median-of-three using comparisons only (no full sort requirement)
    if a <= b <= c or c <= b <= a:
        return b
    if b <= a <= c or c <= a <= b:
        return a
    return c


# =====================================================================================
# LEVEL 5
# =====================================================================================

def expr_41_distance_2d(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.hypot(x2 - x1, y2 - y1)


def expr_42_quadratic_discriminant(a: int | float, b: int | float, c: int | float) -> float:
    return b * b - 4 * a * c


def expr_47_closest_multiple(n: int, m: int) -> int:
    if m == 0:
        raise ValueError("m must be non-zero")
    k = n // m  # floor division
    lower = k * m
    upper = (k + 1) * m
    # choose the closer; tie -> lower by convention (not used in tests)
    if abs(n - upper) < abs(n - lower):
        return upper
    return lower


def expr_48_normalize_angle_deg(theta: int | float) -> float:
    v = theta % 360
    # Map 360 -> 0 implicitly via %
    return 0 if v == 360 else v


def expr_49_piecewise_linear(x: int | float) -> float:
    # As used in tests:
    #   x <= 0        : y = 2x + 1
    #   0 < x < 3     : y = x^2
    #   x >= 3        : y = 3x - 2
    if x <= 0:
        return 2 * x + 1
    if x < 3:
        return x * x
    return 3 * x - 2


def expr_50_quartiles_index(n: int) -> Tuple[int, int, int]:
    if n <= 0:
        raise ValueError("n must be positive")
    # Use floor((n-1)*p) for p in {0.25, 0.5, 0.75}
    k = n - 1
    q1 = (k * 1) // 4
    q2 = (k * 2) // 4
    q3 = (k * 3) // 4
    return (q1, q2, q3)


# =====================================================================================
# LEVEL 6 — Challenge
# =====================================================================================

def expr_51_branchless_sign(n: int) -> int:
    # bools cast to ints: True->1, False->0
    return (1 if n > 0 else 0) - (1 if n < 0 else 0)


def expr_52_interval_overlap_length(a1: int, a2: int, b1: int, b2: int) -> int:
    left = a1 if a1 >= b1 else b1
    right = a2 if a2 <= b2 else b2
    length = right - left
    return length if length > 0 else 0


def expr_53_divisible_by_11_str(s: str) -> bool:
    # Alternating sum rule using 0-based indices:
    # (sum of digits at even positions) - (sum at odd positions) divisible by 11.
    even = 0
    odd = 0
    for i, ch in enumerate(s):
        d = ord(ch) - ord("0")  # s is assumed digits only per prompt
        if (i % 2) == 0:
            even += d
        else:
            odd += d
    return (even - odd) % 11 == 0


def expr_54_palindrome_alnum_casefold(s: str) -> bool:
    filt = [ch.casefold() for ch in s if ch.isalnum()]
    i, j = 0, len(filt) - 1
    while i < j:
        if filt[i] != filt[j]:
            return False
        i += 1
        j -= 1
    return True


def expr_55_majority_of_five(p: bool, q: bool, r: bool, s: bool, t: bool) -> bool:
    return (1 if p else 0) + (1 if q else 0) + (1 if r else 0) + (1 if s else 0) + (1 if t else 0) >= 3


def expr_56_nearest_multiple_bankers_tie(n: int, m: int) -> int:
    if m <= 0:
        raise ValueError("m must be > 0")
    k = math.floor(n / m)
    lower = k * m
    upper = (k + 1) * m
    dl = abs(n - lower)
    du = abs(n - upper)
    if du < dl:
        return upper
    if dl < du:
        return lower
    # tie: choose the multiple whose quotient is even
    # Two candidates: k (for lower) and k+1 (for upper)
    if (k % 2) == 0:
        return lower
    else:
        return upper


def expr_57_median_of_five(a: int, b: int, c: int, d: int, e: int) -> int:
    arr = [a, b, c, d, e]
    arr.sort()
    return arr[2]


def expr_58_isqrt(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    # Binary search integer sqrt
    lo, hi = 0, max(1, n)
    while lo <= hi:
        mid = (lo + hi) // 2
        sq = mid * mid
        if sq == n:
            return mid
        if sq < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi  # floor sqrt
