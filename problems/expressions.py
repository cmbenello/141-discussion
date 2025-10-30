from __future__ import annotations
from typing import Any, Tuple, List

"""
Expressions Problem Set
-------------------------------------------

Table of Contents
---------------------------------

Level 1:
  - Too easy so faded
  
Level 2:
  - 14  seconds_to_hms
  - 15  wrap_clock_12
  - 16  tax_bracket_flag
  - 17  abs_diff
  - 18  min_of_three
  - 20  round_down_to_multiple

Level 3:
  - 21  digit_sum
  - 24  middle_three
  - 25  ascii_shift_digit
  - 26  toggle_ascii_case
  - 29  head_tail

Level 4:
  - 31  exactly_one_true
  - 32  at_least_two_true
  - 33  safe_divide
  - 34  between_inclusive
  - 35  same_sign
  - 36  majority_parity_even
  - 37  ends_with_vowel
  - 38  is_palindrome_ignoring_case
  - 39  safe_index
  - 40  middle_of_three_sorted

Level 5:
  - 41  distance_2d
  - 42  quadratic_discriminant
  - 47  closest_multiple
  - 48  normalize_angle_deg
  - 49  piecewise_linear
  - 50  quartiles_index

Level 6 — Challenge:
  - 51  branchless_sign
  - 52  interval_overlap_length
  - 53  divisible_by_11_str
  - 54  palindrome_alnum_casefold
  - 55  majority_of_five
  - 56  nearest_multiple_bankers_tie
  - 57  median_of_five
  - 58  isqrt
"""



def expr_14_seconds_to_hms(total: int) -> Tuple[int, int, int]:
    """Convert seconds -> (hours, minutes, seconds) using floor division.

    Examples:
      - expr_14_seconds_to_hms(3661) -> (1, 1, 1)
      - expr_14_seconds_to_hms(59) -> (0, 0, 59)
    Tags: integer-division, modulo, time
    """
    raise ValueError("todo: expr_14_seconds_to_hms")


def expr_15_wrap_clock_12(hour: int) -> int:
    """Return hour on a 12-hour clock where 0 -> 12, 13 -> 1, etc.

    Examples:
      - expr_15_wrap_clock_12(0) -> 12
      - expr_15_wrap_clock_12(13) -> 1
    Tags: modulo, wraparound
    """
    raise ValueError("todo: expr_15_wrap_clock_12")


def expr_16_tax_bracket_flag(income: int) -> int:
    """Return 0 if income<=999, 1 if 1000<=income<=1999, else 2.

    Examples:
      - expr_16_tax_bracket_flag(500) -> 0
      - expr_16_tax_bracket_flag(1500) -> 1
      - expr_16_tax_bracket_flag(3000) -> 2
    Tags: comparisons, piecewise
    """
    raise ValueError("todo: expr_16_tax_bracket_flag")


def expr_17_abs_diff(a: int, b: int) -> int:
    """Return ``|a - b|`` without calling ``abs``.

    Examples:
      - expr_17_abs_diff(10, 3) -> 7
      - expr_17_abs_diff(3, 10) -> 7
    Tags: comparisons, arithmetic
    """
    raise ValueError("todo: expr_17_abs_diff")


def expr_18_min_of_three(a: int, b: int, c: int) -> int:
    """Return the minimum of three integers without using ``min``.

    Examples:
      - expr_18_min_of_three(3, 9, 1) -> 1
      - expr_18_min_of_three(7, 7, 8) -> 7
    Tags: comparisons, selection
    """
    raise ValueError("todo: expr_18_min_of_three")




def expr_20_round_down_to_multiple(n: int, m: int) -> int:
    """Return the greatest multiple of ``m`` not exceeding ``n`` (m>0).

    Examples:
      - expr_20_round_down_to_multiple(27, 10) -> 20
      - expr_20_round_down_to_multiple(30, 7) -> 28
    Tags: modulo, floor, multiples
    """
    raise ValueError("todo: expr_20_round_down_to_multiple")


# =====================================================================================
# LEVEL 3 — Strings as expressions, digits/encoding, small lists/tuples [21–30]
# =====================================================================================

def expr_21_digit_sum(n: int) -> int:
    """Return sum of decimal digits of ``n`` (ignore sign).

    Examples:
      - expr_21_digit_sum(1234) -> 10
      - expr_21_digit_sum(-90) -> 9
    Tags: digits, loops/expressions
    """
    raise ValueError("todo: expr_21_digit_sum")




def expr_24_middle_three(s: str) -> str:
    """Given odd-length string, return the middle 3 chars (assume len>=3 odd).

    Examples:
      - expr_24_middle_three("abcdefg") -> 'def'
    Tags: strings, indexing, slicing
    """
    raise ValueError("todo: expr_24_middle_three")


def expr_25_ascii_shift_digit(ch: str, k: int) -> str:
    """If ``ch`` is '0'..'9', shift by k (wrap mod 10), else return ``ch``.

    Examples:
      - expr_25_ascii_shift_digit('9', 1) -> '0'
      - expr_25_ascii_shift_digit('3', -5) -> '8'
    Tags: digits, ascii, wraparound
    """
    raise ValueError("todo: expr_25_ascii_shift_digit")


def expr_26_toggle_ascii_case(ch: str) -> str:
    """Toggle case if ``ch`` is A–Z or a–z; otherwise return ``ch``.

    Examples:
      - expr_26_toggle_ascii_case('A') -> 'a'
      - expr_26_toggle_ascii_case('q') -> 'Q'
      - expr_26_toggle_ascii_case('!') -> '!'
    Tags: ascii, case, strings
    """
    raise ValueError("todo: expr_26_toggle_ascii_case")




def expr_29_head_tail(lst: List[Any]) -> Tuple[Any, List[Any]]:
    """Assume ``len(lst)>0``. Return ``(first_element, rest_list)``.

    Examples:
      - expr_29_head_tail([1,2,3]) -> (1, [2,3])
    Tags: lists, slicing
    """
    raise ValueError("todo: expr_29_head_tail")




# =====================================================================================
# LEVEL 4 — Boolean logic, short-circuit, guards, mixed types [31–40]
# =====================================================================================

def expr_31_exactly_one_true(p: bool, q: bool, r: bool) -> bool:
    """Return True iff exactly one of ``p,q,r`` is True.

    Examples:
      - expr_31_exactly_one_true(True, False, False) -> True
      - expr_31_exactly_one_true(True, True, False) -> False
    Tags: boolean, xor, counting
    """
    raise ValueError("todo: expr_31_exactly_one_true")


def expr_32_at_least_two_true(p: bool, q: bool, r: bool) -> bool:
    """Return True iff at least two of ``p,q,r`` are True.

    Examples:
      - expr_32_at_least_two_true(False, True, True) -> True
      - expr_32_at_least_two_true(True, False, False) -> False
    Tags: boolean, thresholds
    """
    raise ValueError("todo: expr_32_at_least_two_true")


def expr_33_safe_divide(n: int, d: int, default: float = 0.0) -> float:
    """Return ``n/d`` unless ``d==0``, in which case return ``default``.

    Examples:
      - expr_33_safe_divide(6, 3) -> 2.0
      - expr_33_safe_divide(7, 0, default=1.5) -> 1.5
    Tags: guard, division, short-circuit
    """
    raise ValueError("todo: expr_33_safe_divide")


def expr_34_between_inclusive(x: int, lo: int, hi: int) -> bool:
    """Return True iff ``lo <= x <= hi``.

    Examples:
      - expr_34_between_inclusive(5, 5, 9) -> True
      - expr_34_between_inclusive(4, 5, 9) -> False
    Tags: comparisons, chaining
    """
    raise ValueError("todo: expr_34_between_inclusive")


def expr_35_same_sign(a: int, b: int) -> bool:
    """Return True iff ``a`` and ``b`` have the same sign (treat 0 as non-negative).

    Examples:
      - expr_35_same_sign(3, 0) -> True
      - expr_35_same_sign(-2, 5) -> False
    Tags: comparisons, sign
    """
    raise ValueError("todo: expr_35_same_sign")


def expr_36_majority_parity_even(a: int, b: int, c: int) -> bool:
    """Return True iff at least two of ``a,b,c`` are even.

    Examples:
      - expr_36_majority_parity_even(2, 4, 5) -> True
      - expr_36_majority_parity_even(1, 3, 5) -> False
    Tags: parity, counting
    """
    raise ValueError("todo: expr_36_majority_parity_even")


def expr_37_ends_with_vowel(s: str) -> bool:
    """Return True iff the last character of ``s`` is a vowel (aeiou, case-insensitive).

    Assume ``len(s)>0``.
    Examples:
      - expr_37_ends_with_vowel("Caro") -> True
      - expr_37_ends_with_vowel("Sky") -> False
    Tags: strings, indexing, vowels
    """
    raise ValueError("todo: expr_37_ends_with_vowel")


def expr_38_is_palindrome_ignoring_case(s: str) -> bool:
    """Return True iff ``s`` is a palindrome ignoring ASCII case.

    Examples:
      - expr_38_is_palindrome_ignoring_case("Level") -> True
      - expr_38_is_palindrome_ignoring_case("abc") -> False
    Tags: strings, slicing, case-fold
    """
    raise ValueError("todo: expr_38_is_palindrome_ignoring_case")


def expr_39_safe_index(lst: List[Any], idx: int, default: Any = None) -> Any:
    """Return ``lst[idx]`` if in range, else ``default``.

    Examples:
      - expr_39_safe_index([10,20], 1, default=-1) -> 20
      - expr_39_safe_index([10,20], 5, default=-1) -> -1
    Tags: lists, bounds-check, guard
    """
    raise ValueError("todo: expr_39_safe_index")


def expr_40_middle_of_three_sorted(a: int, b: int, c: int) -> int:
    """Return the median (middle) value among ``a,b,c`` without using sort.

    Examples:
      - expr_40_middle_of_three_sorted(1, 9, 5) -> 5
      - expr_40_middle_of_three_sorted(7, 7, 9) -> 7
    Tags: comparisons, median, selection
    """
    raise ValueError("todo: expr_40_middle_of_three_sorted")


# =====================================================================================
# LEVEL 5 — Harder expressions, bitwise, numeric tricks, composition [41–50]
# =====================================================================================

def expr_41_distance_2d(x1: float, y1: float, x2: float, y2: float) -> float:
    """Return Euclidean distance between two points in 2D.

    Examples:
      - expr_41_distance_2d(0,0,3,4) -> 5.0
    Tags: arithmetic, sqrt-free (you may use **0.5)
    """
    raise ValueError("todo: expr_41_distance_2d")


def expr_42_quadratic_discriminant(a: float, b: float, c: float) -> float:
    """Return ``b*b - 4*a*c``.

    Examples:
      - expr_42_quadratic_discriminant(1, -3, 2) -> 1.0
    Tags: arithmetic, formulas
    """
    raise ValueError("todo: expr_42_quadratic_discriminant")




def expr_47_closest_multiple(n: int, m: int) -> int:
    """Return the multiple of ``m`` closest to ``n`` (round half up).

    Examples:
      - expr_47_closest_multiple(27, 10) -> 30
      - expr_47_closest_multiple(25, 10) -> 30
    Tags: rounding, multiples
    """
    raise ValueError("todo: expr_47_closest_multiple")


def expr_48_normalize_angle_deg(theta: float) -> float:
    """Normalize degrees to the range [0, 360).

    Examples:
      - expr_48_normalize_angle_deg(-30) -> 330.0
      - expr_48_normalize_angle_deg(725) -> 5.0
    Tags: modulo, wraparound, floats
    """
    raise ValueError("todo: expr_48_normalize_angle_deg")


def expr_49_piecewise_linear(x: float, k: float) -> float:
    """Return piecewise value: ``x`` if ``|x|<=k`` else ``k * sign(x)``.

    Examples:
      - expr_49_piecewise_linear(3.2, 5) -> 3.2
      - expr_49_piecewise_linear(-10, 4) -> -4.0
    Tags: piecewise, clamp, abs
    """
    raise ValueError("todo: expr_49_piecewise_linear")


def expr_50_quartiles_index(n: int) -> Tuple[int, int, int]:
    """Given length ``n`` of a sorted list, return indices of Q1, Q2, Q3
    using floor-based positions: ``(n//4, n//2, (3*n)//4)``.

    Examples:
      - expr_50_quartiles_index(8) -> (2, 4, 6)
      - expr_50_quartiles_index(9) -> (2, 4, 6)
    Tags: integer-division, indices, statistics
    """
    raise ValueError("todo: expr_50_quartiles_index")



# =====================================================================================
# LEVEL 6 — Challenge [51–58]
# =====================================================================================

def expr_51_branchless_sign(n: int) -> int:
    """Return -1 if n<0, 0 if n==0, 1 if n>0 using only comparisons/arithmetic.

    Examples:
      - expr_51_branchless_sign(-7) -> -1
      - expr_51_branchless_sign(0) -> 0
      - expr_51_branchless_sign(9) -> 1
    Tags: branchless, booleans-as-ints, sign
    """
    raise ValueError("todo: expr_51_branchless_sign")


def expr_52_interval_overlap_length(a1: int, a2: int, b1: int, b2: int) -> int:
    """Given half-open intervals [a1,a2) and [b1,b2), return length of intersection (≥0).

    Examples:
      - expr_52_interval_overlap_length(1, 5, 4, 9) -> 1
      - expr_52_interval_overlap_length(2, 3, 5, 6) -> 0
      - expr_52_interval_overlap_length(0, 10, -3, 2) -> 2
    Tags: piecewise, min/max-without-minmax, ranges
    """
    raise ValueError("todo: expr_52_interval_overlap_length")


def expr_53_divisible_by_11_str(s: str) -> bool:
    """Return True iff the decimal string s is divisible by 11 using alternating-sum rule.

    Assumptions: s consists of digits only (no sign or spaces), len(s)>0.
    Rule: (sum of digits in odd positions) - (sum of digits in even positions) is divisible by 11.
    Examples:
      - expr_53_divisible_by_11_str("121") -> True
      - expr_53_divisible_by_11_str("123") -> False
      - expr_53_divisible_by_11_str("0") -> True
    Tags: digits, modulo, alternating-sum
    """
    raise ValueError("todo: expr_53_divisible_by_11_str")


def expr_54_palindrome_alnum_casefold(s: str) -> bool:
    """Return True iff s is a palindrome when restricted to alphanumerics, ignoring case.

    Examples:
      - expr_54_palindrome_alnum_casefold("Madam, I'm Adam") -> True
      - expr_54_palindrome_alnum_casefold("ab?c") -> False
      - expr_54_palindrome_alnum_casefold("A man, a plan, a canal: Panama") -> True
    Tags: strings, filtering, casefold, slicing
    """
    raise ValueError("todo: expr_54_palindrome_alnum_casefold")


def expr_55_majority_of_five(p: bool, q: bool, r: bool, s: bool, t: bool) -> bool:
    """Return True iff at least three of the five booleans are True.

    Examples:
      - expr_55_majority_of_five(True, True, True, False, False) -> True
      - expr_55_majority_of_five(True, False, False, False, True) -> False
    Tags: counting, booleans-as-ints, thresholds
    """
    raise ValueError("todo: expr_55_majority_of_five")


def expr_56_nearest_multiple_bankers_tie(n: int, m: int) -> int:
    """Return the multiple of m>0 closest to n; if exactly halfway, choose the multiple whose quotient is even.

    Examples:
      - expr_56_nearest_multiple_bankers_tie(27, 10) -> 30
      - expr_56_nearest_multiple_bankers_tie(25, 10) -> 20  # 2 is even
      - expr_56_nearest_multiple_bankers_tie(15, 10) -> 20  # 1.5 rounds up to even-quotient multiple
    Tags: rounding, parity, modulo
    """
    raise ValueError("todo: expr_56_nearest_multiple_bankers_tie")


def expr_57_median_of_five(a: int, b: int, c: int, d: int, e: int) -> int:
    """Return the median (3rd smallest) of five integers without sorting the whole list.

    Examples:
      - expr_57_median_of_five(1, 9, 5, 7, 3) -> 5
      - expr_57_median_of_five(7, 7, 7, 9, 1) -> 7
    Tags: comparisons, selection, median
    """
    raise ValueError("todo: expr_57_median_of_five")


def expr_58_isqrt(n: int) -> int:
    """Return floor(sqrt(n)) for n≥0 using integer operations and a loop (no math module).

    Examples:
      - expr_58_isqrt(0) -> 0
      - expr_58_isqrt(15) -> 3
      - expr_58_isqrt(16) -> 4
    Tags: loops, bounds, integer-arithmetic
    """
    raise ValueError("todo: expr_58_isqrt")

__all__ = [name for name in globals().keys() if name.startswith("expr_")]
