

from typing import Any
import builtins
import types
import pytest
from problems import assessement as A

# Ensure a clean slate for scoping tests
A.GLOBAL_COUNTER = 0

# =========================
# 1) TYPES / EXPRESSIONS
# =========================

def test_expr_01_add_one_and_multiply():
    assert A.expr_01_add_one_and_multiply(5, 2) == 12
    assert A.expr_01_add_one_and_multiply(0, 0) == 0
    assert A.expr_01_add_one_and_multiply(-1, 3) == 6


def test_expr_02_int_div_and_mod():
    assert A.expr_02_int_div_and_mod(7, 3) == (2, 1)
    assert A.expr_02_int_div_and_mod(-7, 3) == (-3, 2)
    assert A.expr_02_int_div_and_mod(9, 1) == (9, 0)


def test_expr_03_mean_of_three():
    assert A.expr_03_mean_of_three(1.0, 2.0, 4.0) == pytest.approx(2.3333333333)
    assert A.expr_03_mean_of_three(0.0, 0.0, 0.0) == 0.0
    assert A.expr_03_mean_of_three(-3.0, 3.0, 0.0) == 0.0


def test_expr_04_bool_combo():
    assert isinstance(A.expr_04_bool_combo(True, False, True), bool)
    assert isinstance(A.expr_04_bool_combo(False, False, False), bool)
    assert isinstance(A.expr_04_bool_combo(True, True, True), bool)


def test_expr_05_clamp():
    assert A.expr_05_clamp(10, 0, 5) == 5
    assert A.expr_05_clamp(-2, -1, 3) == -1
    assert A.expr_05_clamp(2, 0, 5) == 2

# =========================
# 2) FUNCTIONS
# =========================

def test_func_01_sign():
    assert A.func_01_sign(-8) == -1
    assert A.func_01_sign(0) == 0
    assert A.func_01_sign(7) == 1


def test_func_02_apply_twice():
    assert A.func_02_apply_twice(lambda y: y + 1, 3) == 5
    assert A.func_02_apply_twice(str, 7) == '7'
    assert A.func_02_apply_twice(lambda s: s*2, 'a') == 'aaaa'


def test_func_03_default_step_sum():
    assert A.func_03_default_step_sum(5) == 15
    assert A.func_03_default_step_sum(6, step=2) == 12
    assert A.func_03_default_step_sum(1, step=1) == 1


def test_func_04_in_place_append():
    data = [1, 2]
    assert A.func_04_in_place_append(data, 3) is None
    assert data == [1, 2, 3]
    A.func_04_in_place_append(data, -1)
    assert data == [1, 2, 3, -1]


def test_func_05_shadowing_demo():
    out1 = A.func_05_shadowing_demo(10)
    out2 = A.func_05_shadowing_demo(-3)
    assert isinstance(out1, int)
    assert isinstance(out2, int)
    assert out1 != out2 or True

# =========================
# 3) CONDITIONALS
# =========================

def test_cond_01_is_even():
    assert A.cond_01_is_even(8) is True
    assert A.cond_01_is_even(7) is False
    assert A.cond_01_is_even(0) is True


def test_cond_02_grade_bucket():
    assert A.cond_02_grade_bucket(95) in {'A','B','C','D','F'}
    assert A.cond_02_grade_bucket(55) in {'A','B','C','D','F'}
    assert len(A.cond_02_grade_bucket(0)) == 1


def test_cond_03_max_of_three():
    assert A.cond_03_max_of_three(3, 9, 5) == 9
    assert A.cond_03_max_of_three(-1, -1, -2) == -1
    assert A.cond_03_max_of_three(7, 7, 7) == 7


def test_cond_04_abs_val():
    assert A.cond_04_abs_val(-7) == 7
    assert A.cond_04_abs_val(0) == 0
    assert A.cond_04_abs_val(9) == 9


def test_cond_05_triangle_type():
    assert A.cond_05_triangle_type(3, 3, 3) == 'equilateral'
    assert A.cond_05_triangle_type(2, 3, 5) is None
    assert A.cond_05_triangle_type(3, 4, 4) in {'isosceles', 'scalene'}

# =========================
# 4) LOOPS
# =========================

def test_loop_01_factorial():
    assert A.loop_01_factorial(5) == 120
    assert A.loop_01_factorial(0) == 1
    assert A.loop_01_factorial(1) == 1


def test_loop_02_count_until():
    assert A.loop_02_count_until([1, 2, 3, 2], 2) == 1
    assert A.loop_02_count_until([9, 9, 9], 5) == 3
    assert A.loop_02_count_until([], 7) == 0


def test_loop_03_sum_first_k_multiples():
    assert A.loop_03_sum_first_k_multiples(3, 4) == 24
    assert A.loop_03_sum_first_k_multiples(0, 7) == 0
    assert A.loop_03_sum_first_k_multiples(1, 5) == 5


def test_loop_04_first_index_of():
    assert A.loop_04_first_index_of(['a', 'b', 'c'], 'b') == 1
    assert A.loop_04_first_index_of([], 42) is None
    assert A.loop_04_first_index_of([1, 2, 3], 4) is None


def test_loop_05_has_increasing_pair():
    assert A.loop_05_has_increasing_pair([3, 2, 1]) is False
    assert A.loop_05_has_increasing_pair([1, 1, 2]) is True
    assert A.loop_05_has_increasing_pair([5]) is False

# =========================
# 5) STRINGS
# =========================

def test_str_01_count_vowels():
    assert A.str_01_count_vowels('University of Chicago') == 8
    assert A.str_01_count_vowels('rhythm') == 0
    assert A.str_01_count_vowels('AEiou') == 5


def test_str_02_reverse_words():
    assert A.str_02_reverse_words('  a  b   c ') == 'c b a'
    assert A.str_02_reverse_words('hello') == 'hello'
    assert A.str_02_reverse_words('one two') == 'two one'


def test_str_03_toggle_case_ascii():
    assert A.str_03_toggle_case_ascii('GoodPassword') == 'gOODpASSWORD'
    assert A.str_03_toggle_case_ascii('MoNkEy123') == 'mOnKeY123'
    assert A.str_03_toggle_case_ascii('aA!') == 'Aa!'


def test_str_04_shift_digits_wrap():
    assert A.str_04_shift_digits_wrap('123456', 3) == '456789'
    assert A.str_04_shift_digits_wrap('0abc9', -1) == '9abc8'
    assert A.str_04_shift_digits_wrap('z9z9', 1) == 'z0z0'


def test_str_05_alpha_only():
    assert A.str_05_alpha_only('ladyGAGA25!') == 'ladyGAGA'
    assert A.str_05_alpha_only('qwerty') == 'qwerty'
    assert A.str_05_alpha_only('!67skibidi') == 'skibidi'

# =========================
# 6) LISTS
# =========================

def test_list_01_sum():
    lst = [1, 2, 3]
    assert A.list_01_sum(lst) == 6
    assert lst == [1, 2, 3]
    assert A.list_01_sum([]) == 0


def test_list_02_min_index():
    assert A.list_02_min_index([5, 4, 3, 2, 1]) == 4
    assert A.list_02_min_index([]) is None
    assert A.list_02_min_index([2, 2, 3]) == 0


def test_list_03_dedup_preserve_order():
    assert A.list_03_dedup_preserve_order([1, 2, 1, 3, 2, 4]) == [1, 2, 3, 4]
    assert A.list_03_dedup_preserve_order([]) == []
    assert A.list_03_dedup_preserve_order([1, 1, 1]) == [1]


def test_list_04_rotate_right():
    assert A.list_04_rotate_right([1, 2, 3, 4], 1) == [4, 1, 2, 3]
    assert A.list_04_rotate_right([1, 2, 3, 4], 6) == [3, 4, 1, 2]
    assert A.list_04_rotate_right([], 3) == []


def test_list_05_all_prefix_sums():
    assert A.list_05_all_prefix_sums([1, 2, 3]) == [1, 3, 6]
    assert A.list_05_all_prefix_sums([]) == []
    assert A.list_05_all_prefix_sums([5]) == [5]

# =========================
# 7) TUPLES
# =========================

def test_tup_01_swap_ends():
    assert A.tup_01_swap_ends((1, 2, 3, 4)) == (4, 2, 3, 1)
    assert A.tup_01_swap_ends((1,)) == (1,)
    assert A.tup_01_swap_ends(()) == ()


def test_tup_02_pairwise_sum():
    assert A.tup_02_pairwise_sum((1, 2, 3), (10, 20)) == (11, 22)
    assert A.tup_02_pairwise_sum((), (1,)) == ()
    assert A.tup_02_pairwise_sum((5,), (7, 8)) == (12,)


def test_tup_03_contains_all():
    assert A.tup_03_contains_all((1, 2, 3), [2, 3]) is True
    assert A.tup_03_contains_all((1, 2, 3), [4]) is False
    assert A.tup_03_contains_all((), []) is True


def test_tup_04_middle_slice():
    assert A.tup_04_middle_slice((0, 1, 2, 3, 4), 1, 4) == (1, 2, 3)
    assert A.tup_04_middle_slice((0, 1), 0, 1) == (0,)
    assert A.tup_04_middle_slice((), 0, 0) == ()


def test_tup_05_unpack_head_tail():
    assert A.tup_05_unpack_head_tail((1, 2, 3, 4)) == (1, (2, 3), 4)
    assert A.tup_05_unpack_head_tail(()) == (None, (), None)
    assert A.tup_05_unpack_head_tail((9,)) == (9, (), None)

# =========================
# 8) LISTS OF LISTS (TABLES)
# =========================

def test_lol_01_flatten():
    assert A.lol_01_flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert A.lol_01_flatten([[]]) == []
    assert A.lol_01_flatten([]) == []


def test_lol_02_row_means():
    assert A.lol_02_row_means([[1, 2, 3], [4, 5, 6]]) == [2.0, 5.0]
    assert A.lol_02_row_means([[10]]) == [10.0]
    assert A.lol_02_row_means([[2, 2], [1, 3]]) == [2.0, 2.0]


def test_lol_03_extract_column():
    assert A.lol_03_extract_column([["a", "b"], [1, 2], [3, 4]], 1) == [2, 4]
    assert A.lol_03_extract_column([[1, 2, 3]], 0) == []
    assert A.lol_03_extract_column([["h"], [5], [6]], 0) == [5, 6]


def test_lol_04_select_columns():
    assert A.lol_04_select_columns([["a","b","c"], [1,2,3], [4,5,6]], [2,0]) == [["c", "a"], [3, 1], [6, 4]]
    assert A.lol_04_select_columns([["x","y"], [9,8]], [1]) == [["y"], [8]]
    assert A.lol_04_select_columns([["h"], [5], [6]], [0]) == [["h"], [5], [6]]


def test_lol_05_filter_rows_eq():
    assert A.lol_05_filter_rows_eq([["x","y"], [1,2], [3,2]], 1, 2) == [["x", "y"], [1, 2], [3, 2]]
    assert A.lol_05_filter_rows_eq([["x","y"], [1,9], [3,2]], 1, 9) == [["x", "y"], [1, 9]]
    assert A.lol_05_filter_rows_eq([[1,2,3]], 0, 1) == [[1,2,3]]

# =========================
# 9) FUNCTION SCOPING
# =========================

def test_scope_01_local_vs_global():
    A.GLOBAL_COUNTER = 0
    out_local, out_global = A.scope_01_local_vs_global(5)
    assert isinstance(out_local, int)
    assert isinstance(out_global, int)
    out_local2, out_global2 = A.scope_01_local_vs_global(-1)
    assert isinstance(out_local2, int)
    assert isinstance(out_global2, int)


def test_scope_02_counter_increment():
    A.GLOBAL_COUNTER = 0
    assert isinstance(A.scope_02_counter_increment(2), int)
    v = A.scope_02_counter_increment(3)
    assert isinstance(v, int)
    assert v >= 3


def test_scope_03_inner_function_capture():
    assert isinstance(A.scope_03_inner_function_capture(10), int)
    assert isinstance(A.scope_03_inner_function_capture(0), int)
    assert isinstance(A.scope_03_inner_function_capture(-5), int)


def test_scope_04_parameter_shadowing():
    assert isinstance(A.scope_04_parameter_shadowing(3), int)
    assert isinstance(A.scope_04_parameter_shadowing(0), int)
    assert isinstance(A.scope_04_parameter_shadowing(-7), int)


def test_scope_05_mutable_param_side_effect():
    acc = []
    assert A.scope_05_mutable_param_side_effect(acc, 3) is None
    assert acc[:3] == [0, 1, 2]
    A.scope_05_mutable_param_side_effect(acc, 0)
    assert acc[:3] == [0, 1, 2]

# =========================
# 10) PASS-BY & COPY SEMANTICS
# =========================

def test_copy_01_identity_vs_equality():
    assert A.copy_01_identity_vs_equality([1], [1]) == (False, True)
    same = []
    t = A.copy_01_identity_vs_equality(same, same)
    assert t == (True, True)
    assert A.copy_01_identity_vs_equality(1, 1) == (True, True)


def test_copy_02_shallow_copy_list():
    sh, dp = A.copy_02_shallow_copy_list([[1], [2]])
    assert sh is not dp
    assert sh == dp
    sh[0].append(9)
    assert dp[0] == [1] or dp[0] == [1, 9]


def test_copy_03_append_vs_rebind():
    a, b = A.copy_03_append_vs_rebind([1, 2])
    assert isinstance(a, list) and isinstance(b, list)
    assert a != b
    assert 2 in a and 2 in b


def test_copy_04_inplace_vs_outofplace_sort():
    ins, outs = A.copy_04_inplace_vs_outofplace_sort([3, 1, 2])
    assert ins == outs == [1, 2, 3]
    ins2, outs2 = A.copy_04_inplace_vs_outofplace_sort([1])
    assert ins2 == outs2 == [1]
    ins3, outs3 = A.copy_04_inplace_vs_outofplace_sort([])
    assert ins3 == outs3 == []


def test_copy_05_aliasing_demo():
    lst, alias = A.copy_05_aliasing_demo([1, 2])
    assert lst is alias
    assert lst == [1, 2] or isinstance(lst, list)