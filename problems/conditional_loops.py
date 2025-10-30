"""
CMSC 14100 — Conditionals & Loops Practice Set
---------------------------------------------
40 problems focusing on branching, iteration, and boolean reasoning.

Students should solve using `if`, `elif`, `else`, and loops as appropriate.
Avoid importing libraries unless otherwise specified.
"""

# ------------------ Basic conditionals (1–10) ------------------

def cl01_sign(n: int) -> str:
    """Return 'positive', 'negative', or 'zero' for n."""
    raise ValueError("todo: cl01_sign")


def cl02_max2(a: int, b: int) -> int:
    """Return the larger of a and b using if-else."""
    raise ValueError("todo: cl02_max2")


def cl03_abs_val(n: int) -> int:
    """Return |n| using if instead of abs()."""
    raise ValueError("todo: cl03_abs_val")


def cl04_min3(a: int, b: int, c: int) -> int:
    """Return minimum of three integers."""
    raise ValueError("todo: cl04_min3")


def cl05_same_sign(a: int, b: int) -> bool:
    """True iff both a and b are nonnegative or both nonpositive."""
    raise ValueError("todo: cl05_same_sign")


def cl06_grade(score: float) -> str:
    """Return letter grade A/B/C/D/F using standard 90-80-70-60 cutoffs."""
    raise ValueError("todo: cl06_grade")


def cl07_parity_word(n: int) -> str:
    """Return 'even' or 'odd'."""
    raise ValueError("todo: cl07_parity_word")


def cl08_sign_magnitude(x: int) -> tuple[str, int]:
    """Return (sign, magnitude) where sign is '+', '-', or '0'."""
    raise ValueError("todo: cl08_sign_magnitude")


def cl09_compare(a: int, b: int) -> str:
    """Return 'less', 'equal', or 'greater'."""
    raise ValueError("todo: cl09_compare")


def cl10_safe_div(a: float, b: float) -> float | None:
    """Return a/b if b != 0 else None."""
    raise ValueError("todo: cl10_safe_div")


# ------------------ Loops: counting and summing (11–20) ------------------

def cl11_sum_n(n: int) -> int:
    """Return sum 1+2+...+n using a loop."""
    raise ValueError("todo: cl11_sum_n")


def cl12_sum_even(n: int) -> int:
    """Return sum of even numbers up to n inclusive."""
    raise ValueError("todo: cl12_sum_even")


def cl13_factorial(n: int) -> int:
    """Return n! (assume n>=0)."""
    raise ValueError("todo: cl13_factorial")


def cl14_count_digits(n: int) -> int:
    """Return number of digits in n (use integer division)."""
    raise ValueError("todo: cl14_count_digits")


def cl15_power(base: int, exp: int) -> int:
    """Return base**exp using a loop (nonnegative exp)."""
    raise ValueError("todo: cl15_power")


def cl16_sum_list(nums: list[int]) -> int:
    """Sum all numbers in list using a for-loop."""
    raise ValueError("todo: cl16_sum_list")


def cl17_count_negatives(nums: list[int]) -> int:
    """Return count of negative numbers in list."""
    raise ValueError("todo: cl17_count_negatives")


def cl18_product_list(nums: list[int]) -> int:
    """Return product of all numbers (1 if empty)."""
    raise ValueError("todo: cl18_product_list")


def cl19_contains_zero(nums: list[int]) -> bool:
    """Return True if 0 appears in nums, else False."""
    raise ValueError("todo: cl19_contains_zero")


def cl20_first_even(nums: list[int]) -> int | None:
    """Return first even number or None if none exist."""
    raise ValueError("todo: cl20_first_even")


# ------------------ Nested loops and conditionals (21–30) ------------------

def cl21_multiplication_table(n: int) -> list[list[int]]:
    """Return an n×n multiplication table (list of lists)."""
    raise ValueError("todo: cl21_multiplication_table")


def cl22_square_pattern(n: int) -> str:
    """Return an n×n square of '*' separated by newlines."""
    raise ValueError("todo: cl22_square_pattern")


def cl23_triangle_pattern(n: int) -> str:
    """Return right triangle pattern of '*' of height n."""
    raise ValueError("todo: cl23_triangle_pattern")


def cl24_sum_nested(lst: list[list[int]]) -> int:
    """Return total sum of all elements in nested list of ints."""
    raise ValueError("todo: cl24_sum_nested")


def cl25_find_min_nested(lst: list[list[int]]) -> int:
    """Return minimum element from nested list of ints."""
    raise ValueError("todo: cl25_find_min_nested")


def cl26_count_vowels(s: str) -> int:
    """Return number of vowels in string s."""
    raise ValueError("todo: cl26_count_vowels")


def cl27_remove_spaces(s: str) -> str:
    """Return s with all spaces removed using loop + concatenation."""
    raise ValueError("todo: cl27_remove_spaces")


def cl28_reverse_string(s: str) -> str:
    """Return reversed string using loop (no slicing)."""
    raise ValueError("todo: cl28_reverse_string")


def cl29_is_palindrome(s: str) -> bool:
    """True iff s reads the same forward and backward (case-sensitive)."""
    raise ValueError("todo: cl29_is_palindrome")


def cl30_count_words(s: str) -> int:
    """Return number of words separated by spaces (no split())."""
    raise ValueError("todo: cl30_count_words")


# ------------------ Applied logic & loops (31–40) ------------------

def cl31_fizzbuzz(n: int) -> list[str]:
    """Return FizzBuzz list for 1..n inclusive."""
    raise ValueError("todo: cl31_fizzbuzz")


def cl32_sum_until_negative(nums: list[int]) -> int:
    """Sum numbers until a negative is found (exclusive)."""
    raise ValueError("todo: cl32_sum_until_negative")


def cl33_index_of_max(nums: list[int]) -> int | None:
    """Return index of first maximum value or None if empty."""
    raise ValueError("todo: cl33_index_of_max")


def cl34_find_primes_upto(n: int) -> list[int]:
    """Return list of primes ≤ n (naive check)."""
    raise ValueError("todo: cl34_find_primes_upto")


def cl35_gcd(a: int, b: int) -> int:
    """Return gcd of a,b using Euclidean algorithm."""
    raise ValueError("todo: cl35_gcd")


def cl36_lcm(a: int, b: int) -> int:
    """Return least common multiple using gcd() result."""
    raise ValueError("todo: cl36_lcm")


def cl37_sum_of_digits(n: int) -> int:
    """Return sum of digits of n (nonnegative)."""
    raise ValueError("todo: cl37_sum_of_digits")


def cl38_binary_to_decimal(bits: str) -> int:
    """Convert binary string (e.g., '1011') to decimal int."""
    raise ValueError("todo: cl38_binary_to_decimal")


def cl39_guess_number(secret: int, guesses: list[int]) -> str:
    """Return feedback string: first 'correct', else last guess relation ('too high'/'too low')."""
    raise ValueError("todo: cl39_guess_number")


def cl40_collatz_steps(n: int) -> int:
    """Return number of steps to reach 1 via Collatz sequence."""
    raise ValueError("todo: cl40_collatz_steps")


# ------------------ Searching & scanning (41–45) ------------------

def cl41_count_substring(s: str, t: str) -> int:
    """Return how many times string t appears in s (allow overlaps); do not use find()/count()."""
    raise ValueError("todo: cl41_count_substring")


def cl42_first_index(s: str, ch: str) -> int | None:
    """Return index of first occurrence of single-character ch in s, or None if absent; no index()/find()."""
    raise ValueError("todo: cl42_first_index")


def cl43_run_length_encode(s: str) -> str:
    """Return run-length encoding, e.g., 'aaabb' -> 'a3b2'; singletons still include '1'."""
    raise ValueError("todo: cl43_run_length_encode")


def cl44_has_increasing_triplet(nums: list[int]) -> bool:
    """Return True if there exist i<j<k with nums[i] < nums[j] < nums[k] (O(n) or O(n^2) allowed)."""
    raise ValueError("todo: cl44_has_increasing_triplet")


def cl45_all_unique_chars(s: str) -> bool:
    """Return True iff all characters in s are unique; do not use set()."""
    raise ValueError("todo: cl45_all_unique_chars")


# ------------------ Mixed challenges (46–50) ------------------

def cl46_bounded_while_sum(limit: int) -> int:
    """Using a while-loop, sum 1+2+...+k while the running total <= limit; return the final sum (<= limit)."""
    raise ValueError("todo: cl46_bounded_while_sum")


def cl47_two_sum_exists(nums: list[int], target: int) -> bool:
    """Return True if there exist i!=j with nums[i]+nums[j]==target; O(n^2) nested loops, no sets/dicts."""
    raise ValueError("todo: cl47_two_sum_exists")


def cl48_matrix_trace(mat: list[list[int]]) -> int:
    """Return sum of the main diagonal entries of a square matrix mat using loops (no sum() on slices)."""
    raise ValueError("todo: cl48_matrix_trace")


def cl49_remove_consecutive_duplicates(s: str) -> str:
    """Return s with any run of repeated characters collapsed to a single character."""
    raise ValueError("todo: cl49_remove_consecutive_duplicates")


def cl50_is_sorted_non_decreasing(nums: list[int]) -> bool:
    """Return True iff nums is sorted in non-decreasing order using a loop and comparisons."""
    raise ValueError("todo: cl50_is_sorted_non_decreasing")

# End of file