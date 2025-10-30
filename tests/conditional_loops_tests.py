
import os
import importlib
import pytest

USE_SOLUTIONS = os.getenv("USE_SOLUTIONS") == "1"

if USE_SOLUTIONS:
    cl = importlib.import_module("solutions.conditional_loops_sols")
else:
    cl = importlib.import_module("problems.conditional_loops")


# =====================================================================================
# 1) Numeric Iteration & Accumulation
# =====================================================================================

def test_cl_01_sum_even_up_to():
    assert cl.cl_01_sum_even_up_to(6) == 12
    assert cl.cl_01_sum_even_up_to(-5) == -6
    assert cl.cl_01_sum_even_up_to(0) == 0
    assert cl.cl_01_sum_even_up_to(1) == 0
    assert cl.cl_01_sum_even_up_to(10) == 30

def test_cl_02_product_multiples_range():
    assert cl.cl_02_product_multiples_range(1, 10, 3) == 162
    assert cl.cl_02_product_multiples_range(5, 7, 10) == 1
    assert cl.cl_02_product_multiples_range(3, 3, 3) == 3
    assert cl.cl_02_product_multiples_range(0, 5, 2) == 0
    assert cl.cl_02_product_multiples_range(-6, -1, 3) == 18

def test_cl_13_collatz_steps():
    assert cl.cl_13_collatz_steps(1, 10) == 0
    assert cl.cl_13_collatz_steps(3, 100) == 7
    assert cl.cl_13_collatz_steps(6, 10) == 8
    assert cl.cl_13_collatz_steps(7, 16) == 16
    assert cl.cl_13_collatz_steps(7, 10) == 10

def test_cl_14_gcd_euclid():
    assert cl.cl_14_gcd_euclid(54, 24) == 6
    assert cl.cl_14_gcd_euclid(7, 1) == 1
    assert cl.cl_14_gcd_euclid(0, 5) == 5
    assert cl.cl_14_gcd_euclid(10, 0) == 10
    assert cl.cl_14_gcd_euclid(81, 27) == 27

def test_cl_15_pow_int():
    assert cl.cl_15_pow_int(2, 0) == 1
    assert cl.cl_15_pow_int(3, 4) == 81
    assert cl.cl_15_pow_int(5, 1) == 5
    assert cl.cl_15_pow_int(10, 2) == 100
    assert cl.cl_15_pow_int(1, 1000) == 1


# =====================================================================================
# 2) Filtering, Searching & Early Exit
# =====================================================================================

def test_cl_03_count_divisible():
    assert cl.cl_03_count_divisible([3, 6, 7, 12], 3) == 3
    assert cl.cl_03_count_divisible([], 5) == 0
    assert cl.cl_03_count_divisible([10, 20, 25], 10) == 2
    assert cl.cl_03_count_divisible([-6, -3, 9], 3) == 3
    assert cl.cl_03_count_divisible([1, 2, 4], 3) == 0

def test_cl_04_first_index_gt():
    assert cl.cl_04_first_index_gt([1, 5, 5, 9], 5) == 3
    assert cl.cl_04_first_index_gt([1, 2], 10) is None
    assert cl.cl_04_first_index_gt([], 3) is None
    assert cl.cl_04_first_index_gt([10, 11, 12], 9) == 0
    assert cl.cl_04_first_index_gt([1, 3, 3, 3], 3) is None

def test_cl_05_last_index_lt():
    assert cl.cl_05_last_index_lt([1, 5, 5, 9], 5) == 0
    assert cl.cl_05_last_index_lt([], 0) is None
    assert cl.cl_05_last_index_lt([2, 4, 6], 5) == 1
    assert cl.cl_05_last_index_lt([9, 10, 11], 5) is None
    assert cl.cl_05_last_index_lt([1, 2, 3, 4, 5], 5) == 3

def test_cl_06_has_adjacent_equal():
    assert cl.cl_06_has_adjacent_equal([1, 2, 2, 3])
    assert not cl.cl_06_has_adjacent_equal([1, 2, 3])
    assert cl.cl_06_has_adjacent_equal([5, 5])
    assert not cl.cl_06_has_adjacent_equal([])
    assert not cl.cl_06_has_adjacent_equal([1])

def test_cl_07_first_strict_increase_pair():
    assert cl.cl_07_first_strict_increase_pair([5, 4, 3]) is None
    assert cl.cl_07_first_strict_increase_pair([3, 3, 4]) == 1
    assert cl.cl_07_first_strict_increase_pair([1, 2]) == 0
    assert cl.cl_07_first_strict_increase_pair([]) is None
    assert cl.cl_07_first_strict_increase_pair([9]) is None

def test_cl_08_longest_run_equal():
    assert cl.cl_08_longest_run_equal([1,1,2,2,2,3]) == 3
    assert cl.cl_08_longest_run_equal([]) == 0
    assert cl.cl_08_longest_run_equal([1]) == 1
    assert cl.cl_08_longest_run_equal([5,5,5,5]) == 4
    assert cl.cl_08_longest_run_equal([1,2,3,4]) == 1

def test_cl_09_is_alternating_parity():
    assert cl.cl_09_is_alternating_parity([2,5,4,9,6])
    assert not cl.cl_09_is_alternating_parity([2,4,6])
    assert cl.cl_09_is_alternating_parity([1])
    assert cl.cl_09_is_alternating_parity([])
    assert not cl.cl_09_is_alternating_parity([1,3])

def test_cl_10_first_violation_max_step():
    assert cl.cl_10_first_violation_max_step([1,3,5,8,9], 2) == 3
    assert cl.cl_10_first_violation_max_step([1,2,3], 5) is None
    assert cl.cl_10_first_violation_max_step([], 3) is None
    assert cl.cl_10_first_violation_max_step([0,10], 9) == 1
    assert cl.cl_10_first_violation_max_step([1,1,1], 0) is None

def test_cl_11_two_sum_exists():
    assert cl.cl_11_two_sum_exists([1,2,4,6,10], 8)
    assert cl.cl_11_two_sum_exists([1,2,4,6,10], 3)
    assert not cl.cl_11_two_sum_exists([], 5)
    assert cl.cl_11_two_sum_exists([2,3,4,7,8], 10)
    assert cl.cl_11_two_sum_exists([0,1,2,3,4,5], 5)

def test_cl_12_sliding_window_max_sum():
    assert cl.cl_12_sliding_window_max_sum([1,3,-2,5,3], 2) == 8
    assert cl.cl_12_sliding_window_max_sum([5], 1) == 5
    assert cl.cl_12_sliding_window_max_sum([1,2,3,4,5], 3) == 12
    assert cl.cl_12_sliding_window_max_sum([-1,-2,-3], 2) == -3
    with pytest.raises(ValueError):
        cl.cl_12_sliding_window_max_sum([1,2], 3)


# =====================================================================================
# 3) String & Sequence Iteration (1D)
# =====================================================================================

def test_cl_23_count_substring():
    assert cl.cl_23_count_substring("aaaa", "aa") == 3
    assert cl.cl_23_count_substring("abc", "x") == 0
    assert cl.cl_23_count_substring("ababab", "aba") == 2
    assert cl.cl_23_count_substring("xxx", "xx") == 2
    assert cl.cl_23_count_substring("", "a") == 0

def test_cl_24_run_length_encode_counts():
    assert cl.cl_24_run_length_encode_counts("aaabbc") == [('a',3),('b',2),('c',1)]
    assert cl.cl_24_run_length_encode_counts("") == []
    assert cl.cl_24_run_length_encode_counts("a") == [('a',1)]
    assert cl.cl_24_run_length_encode_counts("abbb") == [('a',1),('b',3)]
    assert cl.cl_24_run_length_encode_counts("112233") == [('1',2),('2',2),('3',2)]

def test_cl_25_is_palindrome_ignoring_nonalpha():
    assert cl.cl_25_is_palindrome_ignoring_nonalpha("Madam, I'm Adam")
    assert not cl.cl_25_is_palindrome_ignoring_nonalpha("Chicago")
    assert cl.cl_25_is_palindrome_ignoring_nonalpha("A man, a plan, a canal: Panama")
    assert cl.cl_25_is_palindrome_ignoring_nonalpha("")
    assert cl.cl_25_is_palindrome_ignoring_nonalpha("x")

def test_cl_26_caesar_shift():
    assert cl.cl_26_caesar_shift("Abz!", 1) == "Bca!"
    assert cl.cl_26_caesar_shift("Abz!", -1) == "Zay!"
    assert cl.cl_26_caesar_shift("Hello", 13) == "Uryyb"
    assert cl.cl_26_caesar_shift("Zz", 2) == "Bb"
    assert cl.cl_26_caesar_shift("", 5) == ""

def test_cl_27_all_unique_chars_ascii():
    assert cl.cl_27_all_unique_chars_ascii("abcd")
    assert not cl.cl_27_all_unique_chars_ascii("abca")
    assert cl.cl_27_all_unique_chars_ascii("")
    assert cl.cl_27_all_unique_chars_ascii(" ")
    assert not cl.cl_27_all_unique_chars_ascii("!!")

def test_cl_28_rotate_left():
    assert cl.cl_28_rotate_left([1,2,3,4,5], 2) == [3,4,5,1,2]
    assert cl.cl_28_rotate_left([], 7) == []
    assert cl.cl_28_rotate_left([1,2,3], -1) == [3,1,2]
    assert cl.cl_28_rotate_left([1], 100) == [1]
    assert cl.cl_28_rotate_left([1,2], 3) == [2,1]

def test_cl_29_partition_even_odd_stable():
    assert cl.cl_29_partition_even_odd_stable([5,2,4,7,6]) == ([2,4,6],[5,7])
    assert cl.cl_29_partition_even_odd_stable([]) == ([],[])
    assert cl.cl_29_partition_even_odd_stable([1,3,5]) == ([],[1,3,5])
    assert cl.cl_29_partition_even_odd_stable([2,4,6]) == ([2,4,6],[])
    assert cl.cl_29_partition_even_odd_stable([1,2,3,4]) == ([2,4],[1,3])

def test_cl_30_merge_two_sorted():
    assert cl.cl_30_merge_two_sorted([1,3,5],[2,2,4,6]) == [1,2,2,3,4,5,6]
    assert cl.cl_30_merge_two_sorted([], [1,2]) == [1,2]
    assert cl.cl_30_merge_two_sorted([1,2], []) == [1,2]
    assert cl.cl_30_merge_two_sorted([],[]) == []
    assert cl.cl_30_merge_two_sorted([1,2,3],[4,5,6]) == [1,2,3,4,5,6]


# =====================================================================================
# 4) Patterns & Grids (ASCII Art)
# =====================================================================================

def test_cl_16_triangle_pattern():
    assert cl.cl_16_triangle_pattern(3).strip() == "*\n**\n***"
    assert cl.cl_16_triangle_pattern(0) == ""
    assert cl.cl_16_triangle_pattern(1).strip() == "*"
    assert "****" in cl.cl_16_triangle_pattern(4)
    assert isinstance(cl.cl_16_triangle_pattern(3), str)

def test_cl_17_hollow_box():
    assert "*" in cl.cl_17_hollow_box(5, 4)
    assert cl.cl_17_hollow_box(0,3) == ""
    assert cl.cl_17_hollow_box(3,0) == ""
    assert isinstance(cl.cl_17_hollow_box(2,2), str)
    assert cl.cl_17_hollow_box(5,1).count("\n") >= 0

def test_cl_18_checkerboard():
    out = cl.cl_18_checkerboard(2,4)
    assert "XOXO" in out
    assert "OXOX" in out
    assert cl.cl_18_checkerboard(0,3) == ""
    assert cl.cl_18_checkerboard(1,1) == "X"
    assert isinstance(out,str)

def test_cl_19_right_aligned_triangle():
    assert isinstance(cl.cl_19_right_aligned_triangle(4,"$"),str)
    assert cl.cl_19_right_aligned_triangle(0) == ""
    assert "$$$$" in cl.cl_19_right_aligned_triangle(4,"$")
    assert "#" in cl.cl_19_right_aligned_triangle(3)
    assert len(cl.cl_19_right_aligned_triangle(2).splitlines()) == 2

def test_cl_20_diamond_odd():
    with pytest.raises(ValueError):
        cl.cl_20_diamond_odd(2)
    out = cl.cl_20_diamond_odd(3)
    assert "*" in out
    assert isinstance(out,str)
    assert len(out.splitlines()) == 3
    assert cl.cl_20_diamond_odd(5).count("*") > 0
    with pytest.raises(ValueError):
        cl.cl_20_diamond_odd(0)


# =====================================================================================
# 5) Lists of Lists (Table-ish)
# =====================================================================================

def test_cl_21_multiplication_table():
    assert cl.cl_21_multiplication_table(1) == [[1]]
    assert cl.cl_21_multiplication_table(0) == []
    assert cl.cl_21_multiplication_table(3)[1][2] == 6
    assert isinstance(cl.cl_21_multiplication_table(2),list)
    assert len(cl.cl_21_multiplication_table(3)) == 3

def test_cl_22_fizzbuzz():
    assert cl.cl_22_fizzbuzz(5) == ['1','2','Fizz','4','Buzz']
    assert cl.cl_22_fizzbuzz(0) == []
    assert cl.cl_22_fizzbuzz(1) == ['1']
    assert "FizzBuzz" in cl.cl_22_fizzbuzz(15)
    assert cl.cl_22_fizzbuzz(3)[2] == 'Fizz'
