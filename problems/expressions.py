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
    """
    Category: Time & Arithmetic  | Tags: integer-division, modulo, time  | Difficulty: 2

    Convert a non-negative number of seconds to a tuple `(hours, minutes, seconds)`
    using floor division and modulo. Hours may exceed 24 (no day wrap).

    Args:
        total (int): total seconds, assume `total >= 0`.

    Returns:
        Tuple[int, int, int]: `(h, m, s)` where `0 <= m < 60` and `0 <= s < 60`.

    Examples:
        >>> expr_14_seconds_to_hms(3661)
        (1, 1, 1)
        >>> expr_14_seconds_to_hms(59)
        (0, 0, 59)
    """
    raise ValueError("todo: expr_14_seconds_to_hms")


def expr_15_wrap_clock_12(hour: int) -> int:
    """
    Category: Modular Arithmetic  | Tags: modulo, wraparound  | Difficulty: 1

    Map any integer hour to a 12-hour clock value in {1..12}. In particular, 0 → 12,
    13 → 1, -1 → 11, etc.

    Args:
        hour (int): possibly negative or large hour value.

    Returns:
        int: hour wrapped to the 12-hour clock in the range 1..12.

    Examples:
        >>> expr_15_wrap_clock_12(0)
        12
        >>> expr_15_wrap_clock_12(13)
        1
    """
    raise ValueError("todo: expr_15_wrap_clock_12")


def expr_16_tax_bracket_flag(income: int) -> int:
    """
    Category: Piecewise Logic  | Tags: comparisons, piecewise  | Difficulty: 1

    Return a small flag for coarse tax brackets: 0 if `income <= 999`, 1 if `1000 <= income <= 1999`,
    else 2. Assumes `income` is an integer.

    Args:
        income (int): annual income.

    Returns:
        int: 0, 1, or 2 per the bracket definition.

    Examples:
        >>> expr_16_tax_bracket_flag(500)
        0
        >>> expr_16_tax_bracket_flag(1500)
        1
        >>> expr_16_tax_bracket_flag(3000)
        2
    """
    raise ValueError("todo: expr_16_tax_bracket_flag")


def expr_17_abs_diff(a: int, b: int) -> int:
    """
    Category: Basic Arithmetic  | Tags: comparisons, arithmetic  | Difficulty: 1

    Compute the absolute difference `|a - b|` without calling `abs`.

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: absolute difference of a and b

    Examples:
        >>> expr_17_abs_diff(10, 3)
        7
        >>> expr_17_abs_diff(3, 10)
        7
    """
    raise ValueError("todo: expr_17_abs_diff")


def expr_18_min_of_three(a: int, b: int, c: int) -> int:
    """
    Category: Selection & Comparisons  | Tags: comparisons, selection  | Difficulty: 2

    Return the minimum of three integers without using `min`.

    Args:
        a (int): value 1
        b (int): value 2
        c (int): value 3

    Returns:
        int: the smallest of a, b, c

    Examples:
        >>> expr_18_min_of_three(3, 9, 1)
        1
        >>> expr_18_min_of_three(7, 7, 8)
        7
    """
    raise ValueError("todo: expr_18_min_of_three")




def expr_20_round_down_to_multiple(n: int, m: int) -> int:
    """
    Category: Multiples & Flooring  | Tags: modulo, floor, multiples  | Difficulty: 2

    Return the greatest multiple of `m` not exceeding `n` (assume `m > 0`).

    Args:
        n (int): value to round down
        m (int): positive multiple base

    Returns:
        int: the largest multiple of m less than or equal to n

    Examples:
        >>> expr_20_round_down_to_multiple(27, 10)
        20
        >>> expr_20_round_down_to_multiple(30, 7)
        28
    """
    raise ValueError("todo: expr_20_round_down_to_multiple")


# =====================================================================================
# LEVEL 3 — Strings as expressions, digits/encoding, small lists/tuples [21–30]
# =====================================================================================

def expr_21_digit_sum(n: int) -> int:
    """
    Category: Digits & Encoding  | Tags: digits, loops/expressions  | Difficulty: 2

    Return the sum of decimal digits of `n`; ignore sign. E.g., `-90` has digits 9 and 0.

    Args:
        n (int): integer whose decimal digits are summed

    Returns:
        int: sum of absolute decimal digits

    Examples:
        >>> expr_21_digit_sum(1234)
        10
        >>> expr_21_digit_sum(-90)
        9
    """
    raise ValueError("todo: expr_21_digit_sum")




def expr_24_middle_three(s: str) -> str:
    """
    Category: String Slicing  | Tags: strings, indexing, slicing  | Difficulty: 2

    Given an odd-length string `s` of length at least 3, return the middle three characters.

    Args:
        s (str): odd-length string

    Returns:
        str: the middle three-character substring

    Examples:
        >>> expr_24_middle_three("abcdefg")
        'def'
    """
    raise ValueError("todo: expr_24_middle_three")


def expr_25_ascii_shift_digit(ch: str, k: int) -> str:
    """
    Category: ASCII & Wrapping  | Tags: digits, ascii, wraparound  | Difficulty: 3

    If `ch` is a decimal digit `'0'..'9'`, shift its value by `k` with wraparound modulo 10.
    Otherwise return `ch` unchanged.

    Args:
        ch (str): single character
        k (int): integer shift amount (may be negative)

    Returns:
        str: shifted digit as a character, or the original `ch`

    Examples:
        >>> expr_25_ascii_shift_digit('9', 1)
        '0'
        >>> expr_25_ascii_shift_digit('3', -5)
        '8'
    """
    raise ValueError("todo: expr_25_ascii_shift_digit")


def expr_26_toggle_ascii_case(ch: str) -> str:
    """
    Category: ASCII Case  | Tags: ascii, case, strings  | Difficulty: 2

    Toggle case of the ASCII letter `ch` if it is in A–Z or a–z; otherwise return `ch`.

    Args:
        ch (str): single character

    Returns:
        str: toggled character or original if non-letter

    Examples:
        >>> expr_26_toggle_ascii_case('A')
        'a'
        >>> expr_26_toggle_ascii_case('q')
        'Q'
        >>> expr_26_toggle_ascii_case('!')
        '!'
    """
    raise ValueError("todo: expr_26_toggle_ascii_case")




def expr_29_head_tail(lst: List[Any]) -> Tuple[Any, List[Any]]:
    """
    Category: Lists & Slicing  | Tags: lists, slicing  | Difficulty: 2

    Assume `len(lst) > 0`. Return a tuple `(first_element, rest_list)`.

    Args:
        lst (List[Any]): non-empty list

    Returns:
        Tuple[Any, List[Any]]: first element and the remaining list (may be empty)

    Examples:
        >>> expr_29_head_tail([1, 2, 3])
        (1, [2, 3])
    """
    raise ValueError("todo: expr_29_head_tail")




# =====================================================================================
# LEVEL 4 — Boolean logic, short-circuit, guards, mixed types [31–40]
# =====================================================================================

def expr_31_exactly_one_true(p: bool, q: bool, r: bool) -> bool:
    """
    Category: Boolean Logic  | Tags: boolean, xor, counting  | Difficulty: 2

    Return `True` iff exactly one of `p, q, r` is `True`.

    Args:
        p (bool): first flag
        q (bool): second flag
        r (bool): third flag

    Returns:
        bool: `True` when exactly one flag is `True`

    Examples:
        >>> expr_31_exactly_one_true(True, False, False)
        True
        >>> expr_31_exactly_one_true(True, True, False)
        False
    """
    raise ValueError("todo: expr_31_exactly_one_true")


def expr_32_at_least_two_true(p: bool, q: bool, r: bool) -> bool:
    """
    Category: Boolean Logic  | Tags: boolean, thresholds  | Difficulty: 2

    Return `True` iff at least two of `p, q, r` are `True`.

    Args:
        p (bool): first flag
        q (bool): second flag
        r (bool): third flag

    Returns:
        bool: `True` when two or three flags are `True`

    Examples:
        >>> expr_32_at_least_two_true(False, True, True)
        True
        >>> expr_32_at_least_two_true(True, False, False)
        False
    """
    raise ValueError("todo: expr_32_at_least_two_true")


def expr_33_safe_divide(n: int, d: int, default: float = 0.0) -> float:
    """
    Category: Guards & Short-Circuit  | Tags: guard, division, short-circuit  | Difficulty: 2

    Return `n/d` unless `d == 0`, in which case return `default`.

    Args:
        n (int): numerator
        d (int): denominator (may be zero)
        default (float, optional): value to return when `d == 0` (default: 0.0)

    Returns:
        float: division result or `default`

    Examples:
        >>> expr_33_safe_divide(6, 3)
        2.0
        >>> expr_33_safe_divide(7, 0, default=1.5)
        1.5
    """
    raise ValueError("todo: expr_33_safe_divide")


def expr_34_between_inclusive(x: int, lo: int, hi: int) -> bool:
    """
    Category: Comparisons  | Tags: comparisons, chaining  | Difficulty: 1

    Return `True` iff `lo <= x <= hi`.

    Args:
        x (int): value
        lo (int): lower bound
        hi (int): upper bound

    Returns:
        bool: `True` if within the closed interval, else `False`

    Examples:
        >>> expr_34_between_inclusive(5, 5, 9)
        True
        >>> expr_34_between_inclusive(4, 5, 9)
        False
    """
    raise ValueError("todo: expr_34_between_inclusive")


def expr_35_same_sign(a: int, b: int) -> bool:
    """
    Category: Sign Logic  | Tags: comparisons, sign  | Difficulty: 2

    Return `True` iff `a` and `b` have the same sign; treat 0 as non-negative.

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        bool: `True` if both are non-negative or both negative

    Examples:
        >>> expr_35_same_sign(3, 0)
        True
        >>> expr_35_same_sign(-2, 5)
        False
    """
    raise ValueError("todo: expr_35_same_sign")


def expr_36_majority_parity_even(a: int, b: int, c: int) -> bool:
    """
    Category: Parity & Counting  | Tags: parity, counting  | Difficulty: 2

    Return `True` iff at least two of `a, b, c` are even.

    Args:
        a (int): value 1
        b (int): value 2
        c (int): value 3

    Returns:
        bool: `True` when two or more are even

    Examples:
        >>> expr_36_majority_parity_even(2, 4, 5)
        True
        >>> expr_36_majority_parity_even(1, 3, 5)
        False
    """
    raise ValueError("todo: expr_36_majority_parity_even")


def expr_37_ends_with_vowel(s: str) -> bool:
    """
    Category: String Inspection  | Tags: strings, indexing, vowels  | Difficulty: 1

    Return `True` iff the last character of `s` is a vowel (aeiou, case-insensitive).
    Assume `len(s) > 0`.

    Args:
        s (str): non-empty string

    Returns:
        bool: `True` if last char is vowel, else `False`

    Examples:
        >>> expr_37_ends_with_vowel("Caro")
        True
        >>> expr_37_ends_with_vowel("Sky")
        False
    """
    raise ValueError("todo: expr_37_ends_with_vowel")


def expr_38_is_palindrome_ignoring_case(s: str) -> bool:
    """
    Category: Palindromes  | Tags: strings, slicing, case-fold  | Difficulty: 2

    Return `True` iff `s` is a palindrome ignoring ASCII case.

    Args:
        s (str): input string

    Returns:
        bool: `True` if palindrome ignoring case, else `False`

    Examples:
        >>> expr_38_is_palindrome_ignoring_case("Level")
        True
        >>> expr_38_is_palindrome_ignoring_case("abc")
        False
    """
    raise ValueError("todo: expr_38_is_palindrome_ignoring_case")


def expr_39_safe_index(lst: List[Any], idx: int, default: Any = None) -> Any:
    """
    Category: List Access & Guards  | Tags: lists, bounds-check, guard  | Difficulty: 2

    Return `lst[idx]` if the index is within bounds, else return `default`.

    Args:
        lst (List[Any]): list to index
        idx (int): index (may be out of range)
        default (Any, optional): fallback value (default: None)

    Returns:
        Any: the element at idx or `default`

    Examples:
        >>> expr_39_safe_index([10, 20], 1, default=-1)
        20
        >>> expr_39_safe_index([10, 20], 5, default=-1)
        -1
    """
    raise ValueError("todo: expr_39_safe_index")


def expr_40_middle_of_three_sorted(a: int, b: int, c: int) -> int:
    """
    Category: Selection & Median  | Tags: comparisons, median, selection  | Difficulty: 3

    Return the median (middle) value among `a, b, c` without sorting a container.

    Args:
        a (int): value 1
        b (int): value 2
        c (int): value 3

    Returns:
        int: the middle value

    Examples:
        >>> expr_40_middle_of_three_sorted(1, 9, 5)
        5
        >>> expr_40_middle_of_three_sorted(7, 7, 9)
        7
    """
    raise ValueError("todo: expr_40_middle_of_three_sorted")


# =====================================================================================
# LEVEL 5 — Harder expressions, bitwise, numeric tricks, composition [41–50]
# =====================================================================================

def expr_41_distance_2d(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Category: Geometry  | Tags: arithmetic, distance  | Difficulty: 2

    Return the Euclidean distance between two 2D points.

    Args:
        x1 (float): x of point 1
        y1 (float): y of point 1
        x2 (float): x of point 2
        y2 (float): y of point 2

    Returns:
        float: distance `sqrt((x2-x1)^2 + (y2-y1)^2)`

    Examples:
        >>> expr_41_distance_2d(0, 0, 3, 4)
        5.0
    """
    raise ValueError("todo: expr_41_distance_2d")


def expr_42_quadratic_discriminant(a: float, b: float, c: float) -> float:
    """
    Category: Algebra  | Tags: arithmetic, formulas  | Difficulty: 1

    Return the discriminant `b*b - 4*a*c` of a quadratic `ax^2 + bx + c`.

    Args:
        a (float): quadratic coefficient
        b (float): linear coefficient
        c (float): constant term

    Returns:
        float: discriminant value

    Examples:
        >>> expr_42_quadratic_discriminant(1, -3, 2)
        1.0
    """
    raise ValueError("todo: expr_42_quadratic_discriminant")




def expr_47_closest_multiple(n: int, m: int) -> int:
    """
    Category: Rounding to Multiples  | Tags: rounding, multiples  | Difficulty: 3

    Return the multiple of `m` closest to `n` (round half up). Assumes `m > 0`.

    Args:
        n (int): value to round
        m (int): positive multiple base

    Returns:
        int: closest multiple of m

    Examples:
        >>> expr_47_closest_multiple(27, 10)
        30
        >>> expr_47_closest_multiple(25, 10)
        30
    """
    raise ValueError("todo: expr_47_closest_multiple")


def expr_48_normalize_angle_deg(theta: float) -> float:
    """
    Category: Modular Arithmetic  | Tags: modulo, wraparound, floats  | Difficulty: 2

    Normalize an angle in degrees to the range `[0, 360)`.

    Args:
        theta (float): angle in degrees (may be negative or large)

    Returns:
        float: equivalent angle in `[0, 360)`

    Examples:
        >>> expr_48_normalize_angle_deg(-30)
        330.0
        >>> expr_48_normalize_angle_deg(725)
        5.0
    """
    raise ValueError("todo: expr_48_normalize_angle_deg")


def expr_49_piecewise_linear(x: float, k: float) -> float:
    """
    Category: Clamping / Piecewise  | Tags: piecewise, clamp, abs  | Difficulty: 3

    Return `x` if `|x| <= k`, else `k * sign(x)` (clamp to `[-k, k]`).

    Args:
        x (float): value to clamp
        k (float): non-negative threshold

    Returns:
        float: clamped value

    Examples:
        >>> expr_49_piecewise_linear(3.2, 5)
        3.2
        >>> expr_49_piecewise_linear(-10, 4)
        -4.0
    """
    raise ValueError("todo: expr_49_piecewise_linear")


def expr_50_quartiles_index(n: int) -> Tuple[int, int, int]:
    """
    Category: Simple Statistics  | Tags: integer-division, indices, statistics  | Difficulty: 2

    Given a sorted list length `n`, return the floor-based indices of Q1, Q2, Q3 as `(n//4, n//2, (3*n)//4)`.

    Args:
        n (int): length of the list (assume `n >= 0`)

    Returns:
        Tuple[int, int, int]: indices `(q1, q2, q3)`

    Examples:
        >>> expr_50_quartiles_index(8)
        (2, 4, 6)
        >>> expr_50_quartiles_index(9)
        (2, 4, 6)
    """
    raise ValueError("todo: expr_50_quartiles_index")



# =====================================================================================
# LEVEL 6 — Challenge [51–58]
# =====================================================================================

def expr_51_branchless_sign(n: int) -> int:
    """
    Category: Branchless Logic  | Tags: branchless, booleans-as-ints, sign  | Difficulty: 3

    Return -1 if `n < 0`, 0 if `n == 0`, 1 if `n > 0` using only comparisons/arithmetic.

    Args:
        n (int): integer value

    Returns:
        int: sign of n in {-1, 0, 1}

    Examples:
        >>> expr_51_branchless_sign(-7)
        -1
        >>> expr_51_branchless_sign(0)
        0
        >>> expr_51_branchless_sign(9)
        1
    """
    raise ValueError("todo: expr_51_branchless_sign")


def expr_52_interval_overlap_length(a1: int, a2: int, b1: int, b2: int) -> int:
    """
    Category: Interval Arithmetic  | Tags: piecewise, min/max-without-minmax, ranges  | Difficulty: 3

    Given half-open intervals `[a1, a2)` and `[b1, b2)`, return the length of their intersection (≥ 0).

    Args:
        a1 (int): start of first interval (inclusive)
        a2 (int): end of first interval (exclusive)
        b1 (int): start of second interval (inclusive)
        b2 (int): end of second interval (exclusive)

    Returns:
        int: length of intersection (0 if disjoint)

    Examples:
        >>> expr_52_interval_overlap_length(1, 5, 4, 9)
        1
        >>> expr_52_interval_overlap_length(2, 3, 5, 6)
        0
        >>> expr_52_interval_overlap_length(0, 10, -3, 2)
        2
    """
    raise ValueError("todo: expr_52_interval_overlap_length")


def expr_53_divisible_by_11_str(s: str) -> bool:
    """
    Category: Divisibility Rules  | Tags: digits, modulo, alternating-sum  | Difficulty: 4

    Return `True` iff the decimal string `s` is divisible by 11 using the alternating-sum rule.
    Assume `s` consists only of digits and has length > 0.

    Args:
        s (str): non-empty string of decimal digits

    Returns:
        bool: `True` if divisible by 11, else `False`

    Examples:
        >>> expr_53_divisible_by_11_str("121")
        True
        >>> expr_53_divisible_by_11_str("123")
        False
        >>> expr_53_divisible_by_11_str("0")
        True
    """
    raise ValueError("todo: expr_53_divisible_by_11_str")


def expr_54_palindrome_alnum_casefold(s: str) -> bool:
    """
    Category: Palindromes with Filtering  | Tags: strings, filtering, casefold, slicing  | Difficulty: 3

    Return `True` iff `s` is a palindrome when restricted to alphanumerics, ignoring case.

    Args:
        s (str): input string

    Returns:
        bool: `True` if palindrome under alnum+casefold, else `False`

    Examples:
        >>> expr_54_palindrome_alnum_casefold("Madam, I'm Adam")
        True
        >>> expr_54_palindrome_alnum_casefold("ab?c")
        False
        >>> expr_54_palindrome_alnum_casefold("A man, a plan, a canal: Panama")
        True
    """
    raise ValueError("todo: expr_54_palindrome_alnum_casefold")


def expr_55_majority_of_five(p: bool, q: bool, r: bool, s: bool, t: bool) -> bool:
    """
    Category: Boolean Counting  | Tags: counting, booleans-as-ints, thresholds  | Difficulty: 2

    Return `True` iff at least three of the five booleans are `True`.

    Args:
        p (bool): first flag
        q (bool): second flag
        r (bool): third flag
        s (bool): fourth flag
        t (bool): fifth flag

    Returns:
        bool: `True` if three or more flags are `True`

    Examples:
        >>> expr_55_majority_of_five(True, True, True, False, False)
        True
        >>> expr_55_majority_of_five(True, False, False, False, True)
        False
    """
    raise ValueError("todo: expr_55_majority_of_five")


def expr_56_nearest_multiple_bankers_tie(n: int, m: int) -> int:
    """
    Category: Rounding with Ties  | Tags: rounding, parity, modulo  | Difficulty: 4

    Return the multiple of `m > 0` closest to `n`; if exactly halfway between two multiples,
    choose the multiple whose quotient `n/m` rounds to an even integer (bankers' rounding).

    Args:
        n (int): value to round
        m (int): positive multiple base

    Returns:
        int: nearest multiple with bankers' tie-breaking

    Examples:
        >>> expr_56_nearest_multiple_bankers_tie(27, 10)
        30
        >>> expr_56_nearest_multiple_bankers_tie(25, 10)
        20
        >>> expr_56_nearest_multiple_bankers_tie(15, 10)
        20
    """
    raise ValueError("todo: expr_56_nearest_multiple_bankers_tie")


def expr_57_median_of_five(a: int, b: int, c: int, d: int, e: int) -> int:
    """
    Category: Selection & Median  | Tags: comparisons, selection, median  | Difficulty: 4

    Return the median (3rd smallest) of five integers without sorting an entire list.

    Args:
        a (int): value 1
        b (int): value 2
        c (int): value 3
        d (int): value 4
        e (int): value 5

    Returns:
        int: the median value

    Examples:
        >>> expr_57_median_of_five(1, 9, 5, 7, 3)
        5
        >>> expr_57_median_of_five(7, 7, 7, 9, 1)
        7
    """
    raise ValueError("todo: expr_57_median_of_five")


def expr_58_isqrt(n: int) -> int:
    """
    Category: Integer Math & Loops  | Tags: loops, bounds, integer-arithmetic  | Difficulty: 4

    Return `floor(sqrt(n))` for `n >= 0` using integer operations and a loop (no `math` module).

    Args:
        n (int): non-negative integer

    Returns:
        int: integer square root (floor)

    Examples:
        >>> expr_58_isqrt(0)
        0
        >>> expr_58_isqrt(15)
        3
        >>> expr_58_isqrt(16)
        4
    """
    raise ValueError("todo: expr_58_isqrt")

__all__ = [name for name in globals().keys() if name.startswith("expr_")]
