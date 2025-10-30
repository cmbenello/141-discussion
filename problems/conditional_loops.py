"""
conditional_loops.py

Curated loop-centric problems (exam/LeetCode style) organized with categories, tags, and difficulty.
Each function contains a precise docstring, Args/Returns, and **Examples**.
Student stubs raise ValueError("todo") — solutions live in solutions/conditional_loops_sols.py
and tests resolve to solutions when the environment variable USE_SOLUTIONS=1.
"""

from __future__ import annotations
from typing import List, Tuple, Optional


# =====================================================================================
# Table of Contents
# =====================================================================================
# 1) Numeric Iteration & Accumulation
#    - cl_01_sum_even_up_to
#    - cl_02_product_multiples_range
#    - cl_13_collatz_steps
#    - cl_14_gcd_euclid
#    - cl_15_pow_int
#
# 2) Filtering, Searching & Early Exit
#    - cl_03_count_divisible
#    - cl_04_first_index_gt
#    - cl_05_last_index_lt
#    - cl_06_has_adjacent_equal
#    - cl_07_first_strict_increase_pair
#    - cl_08_longest_run_equal
#    - cl_09_is_alternating_parity
#    - cl_10_first_violation_max_step
#    - cl_11_two_sum_exists
#    - cl_12_sliding_window_max_sum
#
# 3) String & Sequence Iteration (1D)
#    - cl_23_count_substring
#    - cl_24_run_length_encode_counts
#    - cl_25_is_palindrome_ignoring_nonalpha
#    - cl_26_caesar_shift
#    - cl_27_all_unique_chars_ascii
#    - cl_28_rotate_left
#    - cl_29_partition_even_odd_stable
#    - cl_30_merge_two_sorted
#
# 4) Patterns & Grids (ASCII Art)
#    - cl_16_triangle_pattern
#    - cl_17_hollow_box
#    - cl_18_checkerboard
#    - cl_19_right_aligned_triangle
#    - cl_20_diamond_odd
#
# 5) Lists of Lists (Table-ish)
#    - cl_21_multiplication_table
#    - cl_22_fizzbuzz
#
# Note: Some functions conceptually fit multiple categories; we place them by primary skill.
# =====================================================================================


# =====================================================================================
# 1) Numeric Iteration & Accumulation
# =====================================================================================

def cl_01_sum_even_up_to(n: int) -> int:
    """
    Category: Numeric Iteration & Accumulation | Tags: range, accumulation, parity | Difficulty: 1

    Return the sum of all even integers in [0, n] inclusive. If n < 0, sum evens down to n (e.g., n = -3 -> -2).

    Args:
        n (int): endpoint (inclusive)

    Returns:
        int: sum of even integers from 0 to n (or from n to 0 if n < 0)

    Examples:
        >>> cl_01_sum_even_up_to(6)
        12    # 0+2+4+6
        >>> cl_01_sum_even_up_to(-5)
        -6    # -4 + -2 + 0 (but 0 contributes nothing)
    """
    raise ValueError("todo")


def cl_02_product_multiples_range(a: int, b: int, k: int) -> int:
    """
    Category: Numeric Iteration & Accumulation | Tags: range, product, divisibility | Difficulty: 2

    Compute the product of all integers x in the inclusive range [a, b] such that x % k == 0.
    If there are no such x, return 1 (empty-product convention). Assume a <= b and k != 0.

    Args:
        a (int): start (inclusive)
        b (int): end (inclusive)
        k (int): divisor (non-zero)

    Returns:
        int: product of all multiples of k within [a, b], or 1 if none

    Examples:
        >>> cl_02_product_multiples_range(1, 10, 3)
        18    # 3*6
        >>> cl_02_product_multiples_range(5, 7, 10)
        1
    """
    raise ValueError("todo")


def cl_13_collatz_steps(n: int, cap: int) -> int:
    """
    Category: Numeric Iteration & Accumulation | Tags: collatz, loop_bounded | Difficulty: 3

    Compute how many steps it takes to reach 1 under the Collatz map:
      - if n is even -> n = n//2
      - if n is odd  -> n = 3*n + 1
    Stop early if you perform 'cap' steps without reaching 1, and return 'cap'.
    Precondition: n >= 1, cap >= 0.

    Args:
        n (int): starting value (>=1)
        cap (int): maximum steps to simulate

    Returns:
        int: steps taken to reach 1, or 'cap' if 1 not reached in time

    Examples:
        >>> cl_13_collatz_steps(1, 10)
        0
        >>> cl_13_collatz_steps(3, 100)
        7
    """
    raise ValueError("todo")


def cl_14_gcd_euclid(a: int, b: int) -> int:
    """
    Category: Numeric Iteration & Accumulation | Tags: gcd, loop, math | Difficulty: 2

    Compute gcd(a, b) using the iterative Euclidean algorithm.
    gcd(a, 0) == |a|; ensure non-negative result.

    Args:
        a (int)
        b (int)

    Returns:
        int: greatest common divisor

    Examples:
        >>> cl_14_gcd_euclid(54, 24)
        6
        >>> cl_14_gcd_euclid(7, 1)
        1
    """
    raise ValueError("todo")


def cl_15_pow_int(x: int, n: int) -> int:
    """
    Category: Numeric Iteration & Accumulation | Tags: pow, accumulation | Difficulty: 2

    Compute x**n for n >= 0 using repeated multiplication (no built-in pow).
    Precondition: n >= 0.

    Args:
        x (int): base
        n (int): non-negative exponent

    Returns:
        int: x raised to the n

    Examples:
        >>> cl_15_pow_int(2, 0)
        1
        >>> cl_15_pow_int(3, 4)
        81
    """
    raise ValueError("todo")


# =====================================================================================
# 2) Filtering, Searching & Early Exit
# =====================================================================================

def cl_03_count_divisible(lst: List[int], k: int) -> int:
    """
    Category: Filtering, Searching & Early Exit | Tags: count, divisibility | Difficulty: 1

    Count how many elements in lst are divisible by k (assume k != 0).

    Args:
        lst (List[int]): values
        k (int): divisor (non-zero)

    Returns:
        int: count of elements x with x % k == 0

    Examples:
        >>> cl_03_count_divisible([3, 6, 7, 12], 3)
        3
        >>> cl_03_count_divisible([], 5)
        0
    """
    raise ValueError("todo")


def cl_04_first_index_gt(lst: List[int], x: int) -> Optional[int]:
    """
    Category: Filtering, Searching & Early Exit | Tags: search, first_match, early_exit | Difficulty: 2

    Return the first index i such that lst[i] > x, or None if no such index exists.

    Args:
        lst (List[int])
        x (int)

    Returns:
        Optional[int]: first index with value > x, or None

    Examples:
        >>> cl_04_first_index_gt([1, 5, 5, 9], 5)
        3
        >>> cl_04_first_index_gt([1, 2], 10)
        None
    """
    raise ValueError("todo")


def cl_05_last_index_lt(lst: List[int], x: int) -> Optional[int]:
    """
    Category: Filtering, Searching & Early Exit | Tags: search, last_match | Difficulty: 2

    Return the last index i such that lst[i] < x, or None if no such index exists.

    Examples:
        >>> cl_05_last_index_lt([1, 5, 5, 9], 5)
        0
        >>> cl_05_last_index_lt([], 0)
        None
    """
    raise ValueError("todo")


def cl_06_has_adjacent_equal(lst: List[int]) -> bool:
    """
    Category: Filtering, Searching & Early Exit | Tags: validation, adjacent | Difficulty: 1

    Return True iff the list contains two equal adjacent elements.

    Examples:
        >>> cl_06_has_adjacent_equal([1, 2, 2, 3])
        True
        >>> cl_06_has_adjacent_equal([1, 2, 3])
        False
    """
    raise ValueError("todo")


def cl_07_first_strict_increase_pair(lst: List[int]) -> Optional[int]:
    """
    Category: Filtering, Searching & Early Exit | Tags: search, first_match | Difficulty: 2

    Return the first index i such that lst[i] < lst[i+1]. If not found or len(lst) < 2, return None.

    Examples:
        >>> cl_07_first_strict_increase_pair([5, 4, 3])
        None
        >>> cl_07_first_strict_increase_pair([3, 3, 4])
        1
    """
    raise ValueError("todo")


def cl_08_longest_run_equal(lst: List[int]) -> int:
    """
    Category: Filtering, Searching & Early Exit | Tags: runs, scan | Difficulty: 3

    Return the length of the longest run of equal adjacent values.
    For an empty list, return 0. For a 1-element list, return 1.

    Examples:
        >>> cl_08_longest_run_equal([1,1,2,2,2,3])
        3
        >>> cl_08_longest_run_equal([])
        0
    """
    raise ValueError("todo")


def cl_09_is_alternating_parity(lst: List[int]) -> bool:
    """
    Category: Filtering, Searching & Early Exit | Tags: validation, parity, early_exit | Difficulty: 2

    Return True iff the list alternates even/odd/evens… (any starting parity).
    Lists of length < 2 are considered alternating.

    Examples:
        >>> cl_09_is_alternating_parity([2, 5, 4, 9, 6])
        True
        >>> cl_09_is_alternating_parity([2, 4, 6])
        False
    """
    raise ValueError("todo")


def cl_10_first_violation_max_step(lst: List[int], max_step: int) -> Optional[int]:
    """
    Category: Filtering, Searching & Early Exit | Tags: scan, constraint, early_exit | Difficulty: 3

    Given a sequence of integers, return the first index i>0 where abs(lst[i] - lst[i-1]) > max_step.
    Return None if no violation exists or if len(lst) < 2.

    Examples:
        >>> cl_10_first_violation_max_step([1,3,5,8,9], 2)
        3
        >>> cl_10_first_violation_max_step([1,2,3], 5)
        None
    """
    raise ValueError("todo")


def cl_11_two_sum_exists(sorted_lst: List[int], target: int) -> bool:
    """
    Category: Filtering, Searching & Early Exit | Tags: two_pointer, early_exit | Difficulty: 3

    Given a sorted list (non-decreasing), return True iff there exist i<j with sorted_lst[i]+sorted_lst[j]==target.
    Use a classic two-pointer sweep (no sets/dicts).

    Examples:
        >>> cl_11_two_sum_exists([1,2,4,6,10], 8)
        True    # 2+6
        >>> cl_11_two_sum_exists([1,2,4,6,10], 3)
        False
    """
    raise ValueError("todo")


def cl_12_sliding_window_max_sum(lst: List[int], k: int) -> int:
    """
    Category: Filtering, Searching & Early Exit | Tags: sliding_window, accumulation | Difficulty: 4

    Return the maximum sum of any contiguous subarray of length k.
    Raise ValueError if k <= 0 or k > len(lst).

    Examples:
        >>> cl_12_sliding_window_max_sum([1,3,-2,5,3], 2)
        8   # window [5,3]
        >>> cl_12_sliding_window_max_sum([5], 1)
        5
    """
    raise ValueError("todo")


# =====================================================================================
# 3) String & Sequence Iteration (1D)
# =====================================================================================

def cl_23_count_substring(s: str, sub: str) -> int:
    """
    Category: String & Sequence Iteration | Tags: scan, overlapping, substring | Difficulty: 2

    Count overlapping occurrences of 'sub' inside 's'.
    Precondition: len(sub) >= 1.

    Examples:
        >>> cl_23_count_substring("aaaa", "aa")
        3
        >>> cl_23_count_substring("abc", "x")
        0
    """
    raise ValueError("todo")


def cl_24_run_length_encode_counts(s: str) -> List[Tuple[str, int]]:
    """
    Category: String & Sequence Iteration | Tags: run_length, compression | Difficulty: 3

    Return a run-length encoding as a list of (char, count) tuples.

    Examples:
        >>> cl_24_run_length_encode_counts("aaabbc")
        [('a', 3), ('b', 2), ('c', 1)]
        >>> cl_24_run_length_encode_counts("")
        []
    """
    raise ValueError("todo")


def cl_25_is_palindrome_ignoring_nonalpha(s: str) -> bool:
    """
    Category: String & Sequence Iteration | Tags: filter, palindrome, two_pointer | Difficulty: 3

    Return True iff s is a palindrome when considering only alphabetic characters and ignoring case.

    Examples:
        >>> cl_25_is_palindrome_ignoring_nonalpha("Madam, I'm Adam")
        True
        >>> cl_25_is_palindrome_ignoring_nonalpha("Chicago")
        False
    """
    raise ValueError("todo")


def cl_26_caesar_shift(s: str, k: int) -> str:
    """
    Category: String & Sequence Iteration | Tags: ascii, shift, letters_only | Difficulty: 3

    Shift A..Z and a..z by k (can be negative), wrapping within case.
    Non-letters unchanged.

    Examples:
        >>> cl_26_caesar_shift("Abz!", 1)
        'Bca!'
        >>> cl_26_caesar_shift("Abz!", -1)
        'Zay!'
    """
    raise ValueError("todo")


def cl_27_all_unique_chars_ascii(s: str) -> bool:
    """
    Category: String & Sequence Iteration | Tags: ascii, frequency, validation | Difficulty: 3

    Return True iff all characters in s are unique (ASCII only, ord 0..127).
    Do not use set(); use a fixed-size frequency array via loops.

    Examples:
        >>> cl_27_all_unique_chars_ascii("abcd")
        True
        >>> cl_27_all_unique_chars_ascii("abca")
        False
    """
    raise ValueError("todo")


def cl_28_rotate_left(lst: List[int], k: int) -> List[int]:
    """
    Category: String & Sequence Iteration | Tags: rotation, slice_free_loop | Difficulty: 2

    Return a new list equal to lst rotated left by k positions (k can be any int, normalize by len).
    For empty lst, return [].

    Examples:
        >>> cl_28_rotate_left([1,2,3,4,5], 2)
        [3, 4, 5, 1, 2]
        >>> cl_28_rotate_left([], 7)
        []
    """
    raise ValueError("todo")


def cl_29_partition_even_odd_stable(lst: List[int]) -> Tuple[List[int], List[int]]:
    """
    Category: String & Sequence Iteration | Tags: partition, stability | Difficulty: 2

    Return (evens, odds) as two NEW lists, preserving original relative order in each.

    Examples:
        >>> cl_29_partition_even_odd_stable([5,2,4,7,6])
        ([2, 4, 6], [5, 7])
        >>> cl_29_partition_even_odd_stable([])
        ([], [])
    """
    raise ValueError("todo")


def cl_30_merge_two_sorted(a: List[int], b: List[int]) -> List[int]:
    """
    Category: String & Sequence Iteration | Tags: merge, two_pointer | Difficulty: 3

    Merge two sorted lists (non-decreasing) into a new sorted list (like the merge step of merge sort).

    Examples:
        >>> cl_30_merge_two_sorted([1,3,5], [2,2,4,6])
        [1, 2, 2, 3, 4, 5, 6]
        >>> cl_30_merge_two_sorted([], [1,2])
        [1, 2]
    """
    raise ValueError("todo")


# =====================================================================================
# 4) Patterns & Grids (ASCII Art)
# =====================================================================================

def cl_16_triangle_pattern(n: int) -> str:
    """
    Category: Patterns & Grids (ASCII Art) | Tags: pattern_print, triangle | Difficulty: 1

    Produce a left-justified triangle of '*' with rows 1..n (newline-separated). For n <= 0, return "".

    Examples:
        >>> print(cl_16_triangle_pattern(3))
        *
        **
        ***
        <BLANKLINE>
        >>> cl_16_triangle_pattern(0)
        ''
    """
    raise ValueError("todo")


def cl_17_hollow_box(w: int, h: int) -> str:
    """
    Category: Patterns & Grids (ASCII Art) | Tags: pattern_print, rectangle, hollow | Difficulty: 3

    Return a hollow rectangle of '*' of width w and height h using newline separators.
    For w <= 0 or h <= 0, return "".

    Example (w=5, h=4):
        *****
        *   *
        *   *
        *****

    Examples:
        >>> print(cl_17_hollow_box(5, 4))
        *****
        *   *
        *   *
        *****
        <BLANKLINE>
        >>> cl_17_hollow_box(0, 3)
        ''
    """
    raise ValueError("todo")


def cl_18_checkerboard(n: int, m: int) -> str:
    """
    Category: Patterns & Grids (ASCII Art) | Tags: pattern_print, grid | Difficulty: 2

    Return an n-by-m checkerboard string with 'X' and 'O', top-left 'X', rows separated by newlines.
    For non-positive n or m, return "".

    Examples:
        >>> print(cl_18_checkerboard(2, 4))
        XOXO
        OXOX
        <BLANKLINE>
        >>> cl_18_checkerboard(1, 1)
        'X'
    """
    raise ValueError("todo")


def cl_19_right_aligned_triangle(n: int, ch: str = "#") -> str:
    """
    Category: Patterns & Grids (ASCII Art) | Tags: pattern_print, align | Difficulty: 2

    Return a right-aligned triangle with rows 1..n of the given single-character 'ch'.
    For n <= 0, return "".

    Examples:
        >>> print(cl_19_right_aligned_triangle(4, "$"))
           $
          $$
         $$$
        $$$$
        <BLANKLINE>
        >>> cl_19_right_aligned_triangle(0)
        ''
    """
    raise ValueError("todo")


def cl_20_diamond_odd(n: int) -> str:
    """
    Category: Patterns & Grids (ASCII Art) | Tags: pattern_print, diamond, symmetry | Difficulty: 4

    Return a diamond of '*' with maximal width n, where n must be odd and >= 1.
    If n is even or n < 1, raise ValueError.

    Example for n=5:
      *
     ***
    *****
     ***
      *

    Examples:
        >>> print(cl_20_diamond_odd(3))
         *
        ***
         *
        <BLANKLINE>
    """
    raise ValueError("todo")


# =====================================================================================
# 5) Lists of Lists (Table-ish)
# =====================================================================================

def cl_21_multiplication_table(n: int) -> List[List[int]]:
    """
    Category: Lists of Lists (Table-ish) | Tags: table, nested_loops | Difficulty: 2

    Return the n-by-n multiplication table as a list of lists where cell [i][j] == (i+1)*(j+1).
    For n <= 0, return [].

    Examples:
        >>> cl_21_multiplication_table(1)
        [[1]]
        >>> cl_21_multiplication_table(3)
        [[1, 2, 3],
         [2, 4, 6],
         [3, 6, 9]]
    """
    raise ValueError("todo")


def cl_22_fizzbuzz(n: int) -> List[str]:
    """
    Category: Lists of Lists (Table-ish) | Tags: classic, iteration | Difficulty: 1

    Return the classic FizzBuzz sequence for 1..n as a list of strings:
      - 'FizzBuzz' if multiple of 3 and 5
      - 'Fizz'     if multiple of 3 only
      - 'Buzz'     if multiple of 5 only
      - the number itself otherwise

    Examples:
        >>> cl_22_fizzbuzz(5)
        ['1', '2', 'Fizz', '4', 'Buzz']
        >>> cl_22_fizzbuzz(0)
        []
    """
    raise ValueError("todo")
