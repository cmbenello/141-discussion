

import math
import pytest
from problems import expressions as E

# --------------------
# Level 2
# --------------------

def test_expr_14_seconds_to_hms():
    assert E.expr_14_seconds_to_hms(0) == (0, 0, 0)
    assert E.expr_14_seconds_to_hms(59) == (0, 0, 59)
    assert E.expr_14_seconds_to_hms(3661) == (1, 1, 1)

def test_expr_15_wrap_clock_12():
    assert E.expr_15_wrap_clock_12(12) == 12
    assert E.expr_15_wrap_clock_12(13) == 1
    assert E.expr_15_wrap_clock_12(25) == 1

def test_expr_16_tax_bracket_flag():
    assert E.expr_16_tax_bracket_flag(999) == 0.30
    assert E.expr_16_tax_bracket_flag(1500) == 0.40
    assert E.expr_16_tax_bracket_flag(2000) == 0.45

def test_expr_17_abs_diff():
    assert E.expr_17_abs_diff(10, 4) == 6
    assert E.expr_17_abs_diff(-3, 5) == 8
    assert E.expr_17_abs_diff(-7, -2) == 5

def test_expr_18_min_of_three():
    assert E.expr_18_min_of_three(3, 7, 5) == 3
    assert E.expr_18_min_of_three(-1, -5, 2) == -5
    assert E.expr_18_min_of_three(9, 9, 9) == 9

def test_expr_20_round_down_to_multiple():
    assert E.expr_20_round_down_to_multiple(27, 10) == 20
    assert E.expr_20_round_down_to_multiple(100, 25) == 100
    assert E.expr_20_round_down_to_multiple(1, 4) == 0

# --------------------
# Level 3
# --------------------

def test_expr_21_digit_sum():
    assert E.expr_21_digit_sum(0) == 0
    assert E.expr_21_digit_sum(98765) == 35
    assert E.expr_21_digit_sum(-123) == 6

def test_expr_24_middle_three():
    assert E.expr_24_middle_three("abcdef") == "cde"
    assert E.expr_24_middle_three("12345") == "234"
    assert E.expr_24_middle_three("xyzXYZ") == "zXY"

def test_expr_25_ascii_shift_digit():
    assert E.expr_25_ascii_shift_digit("a1b2c3", 1) == "a2b3c4"
    assert E.expr_25_ascii_shift_digit("z9", 1) == "z0"
    assert E.expr_25_ascii_shift_digit("no-digits", 5) == "no-digits"

def test_expr_26_toggle_ascii_case():
    assert E.expr_26_toggle_ascii_case("GoodPassword") == "gOODpASSWORD"
    assert E.expr_26_toggle_ascii_case("ladyGAGA25") == "LADYgaga25"
    assert E.expr_26_toggle_ascii_case("MoNkEy123!") == "mOnKeY123!"

def test_expr_29_head_tail():
    assert E.expr_29_head_tail([1, 2, 3, 4]) == (1, 4)
    assert E.expr_29_head_tail(["a"]) == ("a", "a")
    assert E.expr_29_head_tail([]) == (None, None)

# --------------------
# Level 4
# --------------------

def test_expr_31_exactly_one_true():
    assert E.expr_31_exactly_one_true(True, False, False) is True
    assert E.expr_31_exactly_one_true(False, False, False) is False
    assert E.expr_31_exactly_one_true(True, True, False) is False

def test_expr_32_at_least_two_true():
    assert E.expr_32_at_least_two_true(True, True, False) is True
    assert E.expr_32_at_least_two_true(True, False, False) is False
    assert E.expr_32_at_least_two_true(True, True, True) is True

def test_expr_33_safe_divide():
    assert E.expr_33_safe_divide(10, 2) == 5.0
    assert E.expr_33_safe_divide(7, 0) is None
    assert E.expr_33_safe_divide(-9, 3) == -3.0

def test_expr_34_between_inclusive():
    assert E.expr_34_between_inclusive(5, 1, 10) is True
    assert E.expr_34_between_inclusive(1, 1, 10) is True
    assert E.expr_34_between_inclusive(11, 1, 10) is False

def test_expr_35_same_sign():
    assert E.expr_35_same_sign(5, 10) is True
    assert E.expr_35_same_sign(-3, -4) is True
    assert E.expr_35_same_sign(-1, 0) is False

def test_expr_36_majority_parity_even():
    assert E.expr_36_majority_parity_even([2, 4, 6]) is True
    assert E.expr_36_majority_parity_even([1, 3, 5, 7]) is False
    assert E.expr_36_majority_parity_even([1, 2, 3, 4]) is True  # evens=2, odds=2 -> treat as even-majority?

def test_expr_37_ends_with_vowel():
    assert E.expr_37_ends_with_vowel("Chicago") is True
    assert E.expr_37_ends_with_vowel("Maroons!") is False
    assert E.expr_37_ends_with_vowel("") is False

def test_expr_38_is_palindrome_ignoring_case():
    assert E.expr_38_is_palindrome_ignoring_case("RaceCar") is True
    assert E.expr_38_is_palindrome_ignoring_case("abc") is False
    assert E.expr_38_is_palindrome_ignoring_case("x") is True

def test_expr_39_safe_index():
    assert E.expr_39_safe_index([10, 20, 30], 1) == 20
    assert E.expr_39_safe_index([10, 20, 30], -1) is None
    assert E.expr_39_safe_index([], 0) is None

def test_expr_40_middle_of_three_sorted():
    assert E.expr_40_middle_of_three_sorted(1, 5, 3) == 3
    assert E.expr_40_middle_of_three_sorted(9, 7, 9) == 9
    assert E.expr_40_middle_of_three_sorted(-5, -10, -7) == -7

# --------------------
# Level 5
# --------------------

def test_expr_41_distance_2d():
    assert E.expr_41_distance_2d(0, 0, 3, 4) == pytest.approx(5.0)
    assert E.expr_41_distance_2d(-1, -1, -4, -5) == pytest.approx(5.0)
    assert E.expr_41_distance_2d(2, 3, 2, 3) == pytest.approx(0.0)

def test_expr_42_quadratic_discriminant():
    assert E.expr_42_quadratic_discriminant(1, -3, 2) == 1  # (x-1)(x-2)
    assert E.expr_42_quadratic_discriminant(1, 2, 1) == 0   # (x+1)^2
    assert E.expr_42_quadratic_discriminant(2, 1, 2) == -15

def test_expr_47_closest_multiple():
    assert E.expr_47_closest_multiple(27, 10) == 30
    assert E.expr_47_closest_multiple(24, 10) == 20
    assert E.expr_47_closest_multiple(-3, 5) == -5

def test_expr_48_normalize_angle_deg():
    assert E.expr_48_normalize_angle_deg(0) == 0
    assert E.expr_48_normalize_angle_deg(360) == 0
    assert E.expr_48_normalize_angle_deg(-90) == 270

def test_expr_49_piecewise_linear():
    # Suppose: y = 2x+1 for x<=0; y = x^2 for 0<x<3; y = 3x-2 for x>=3  (based on typical docstring)
    assert E.expr_49_piecewise_linear(-2) == 2 * (-2) + 1
    assert E.expr_49_piecewise_linear(2) == 2 ** 2
    assert E.expr_49_piecewise_linear(3) == 3 * 3 - 2

def test_expr_50_quartiles_index():
    assert E.expr_50_quartiles_index(8) == (1, 3, 5)   # example indices may depend on your spec
    assert E.expr_50_quartiles_index(9) == (2, 4, 6)
    assert E.expr_50_quartiles_index(1) == (0, 0, 0)

# --------------------
# Level 6 — Challenge
# --------------------

def test_expr_51_branchless_sign():
    assert E.expr_51_branchless_sign(-7) == -1
    assert E.expr_51_branchless_sign(0) == 0
    assert E.expr_51_branchless_sign(9) == 1

def test_expr_52_interval_overlap_length():
    assert E.expr_52_interval_overlap_length(1, 5, 4, 9) == 1
    assert E.expr_52_interval_overlap_length(2, 3, 5, 6) == 0
    assert E.expr_52_interval_overlap_length(0, 10, -3, 2) == 2

def test_expr_53_divisible_by_11_str():
    assert E.expr_53_divisible_by_11_str("121") is True
    assert E.expr_53_divisible_by_11_str("123") is False
    assert E.expr_53_divisible_by_11_str("0") is True

def test_expr_54_palindrome_alnum_casefold():
    assert E.expr_54_palindrome_alnum_casefold("Madam, I'm Adam") is True
    assert E.expr_54_palindrome_alnum_casefold("ab?c") is False
    assert E.expr_54_palindrome_alnum_casefold("A man, a plan, a canal: Panama") is True

def test_expr_55_majority_of_five():
    assert E.expr_55_majority_of_five(True, True, True, False, False) is True
    assert E.expr_55_majority_of_five(True, False, False, False, True) is False
    assert E.expr_55_majority_of_five(False, False, False, False, False) is False

def test_expr_56_nearest_multiple_bankers_tie():
    assert E.expr_56_nearest_multiple_bankers_tie(27, 10) == 30
    assert E.expr_56_nearest_multiple_bankers_tie(25, 10) == 20  # tie -> quotient 2 (even)
    assert E.expr_56_nearest_multiple_bankers_tie(15, 10) == 20  # tie -> quotient 2 (even)

def test_expr_57_median_of_five():
    assert E.expr_57_median_of_five(1, 9, 5, 7, 3) == 5
    assert E.expr_57_median_of_five(7, 7, 7, 9, 1) == 7
    assert E.expr_57_median_of_five(10, -1, 0, 5, 2) == 2

def test_expr_58_isqrt():
    assert E.expr_58_isqrt(0) == 0
    assert E.expr_58_isqrt(15) == 3
    assert E.expr_58_isqrt(16) == 4