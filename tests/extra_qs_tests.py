import pytest
from problems import extra_qs as X

# 1) Variable Scope & Namespaces — Guess the Output (x10)

def test_scope_01_shadowing():
    assert X.scope_01_shadowing() == (10, 5)

def test_scope_02_unbound_local():
    assert X.scope_02_unbound_local() == -1

def test_scope_03_global_stmt():
    assert X.scope_03_global_stmt() == ["set x to 99", "after: 99"]

def test_scope_04_nonlocal_chain():
    assert X.scope_04_nonlocal_chain() == ["inner: 3", "outer: 3"]

def test_scope_05_comp_scope():
    assert X.scope_05_comp_scope() == ["y: [0, 1, 2]", "x: 100"]

def test_scope_06_for_var_leaks():
    assert X.scope_06_for_var_leaks() == 1

def test_scope_07_del_name():
    assert X.scope_07_del_name() == ["[1]", "False"]

def test_scope_08_default_capture_time():
    assert X.scope_08_default_capture_time() == 10

def test_scope_09_nested_shadowing():
    assert X.scope_09_nested_shadowing() == ["inner: 3", "outer: 2", "global: 1"]

def test_scope_10_class_scope_lookup():
    assert X.scope_10_class_scope_lookup() == ["class body X = 2", "1 2 2"]


# 2) Mutability & Immutability (x10)

def test_mut_01_list_vs_tuple():
    assert X.mut_01_list_vs_tuple() == ["[1, 99, 3]", "(1, 2, 3)"]

def test_mut_02_string_methods():
    assert X.mut_02_string_methods() == ["t: HELLO", "s: hello"]

def test_mut_03_aliasing():
    assert X.mut_03_aliasing() == "[1, 2, 3] [1, 2, 3] True"

def test_mut_04_tuple_with_list():
    assert X.mut_04_tuple_with_list() == "(1, [2, 3, 4])"

def test_mut_05_frozenset_behavior():
    assert X.mut_05_frozenset_behavior() == ["[1, 2, 3]", "[1, 2]"]

def test_mut_06_bytes_vs_bytearray():
    assert X.mut_06_bytes_vs_bytearray() == ["TypeError", "b'dbc'"]

def test_mut_07_dict_alias_mutation():
    assert X.mut_07_dict_alias_mutation() == "{'x': 1, 'y': 2}"

def test_mut_08_tuple_concat_new_obj():
    assert X.mut_08_tuple_concat_new_obj() == "(1, 2) (1, 2, 3) False"

def test_mut_09_list_copy_method():
    assert X.mut_09_list_copy_method() == "[[1, 9], [2]] [[1, 9], [2]] False"

def test_mut_10_str_replace_creates_new():
    assert X.mut_10_str_replace_creates_new() == ["bonono", "banana"]


# 3) Shallow vs Deep Copy (x10)

def test_copy_01_shallow_top():
    assert X.copy_01_shallow_top() == ["[[99, 2], [3, 4]]", "[[99, 2], [3, 4]]"]

def test_copy_02_deepcopy():
    assert X.copy_02_deepcopy() == ["[[1, 2], [3, 4]]", "[[99, 2], [3, 4]]"]

def test_copy_03_slice_copy():
    assert X.copy_03_slice_copy() == "[[1, 9], [2]] [[1, 9], [2]] False"

def test_copy_04_dict_copy_vs_update():
    assert X.copy_04_dict_copy_vs_update() == "{'x': [1, 2]} {'x': [1, 2]}"

def test_copy_05_nested_tuple_copy():
    assert X.copy_05_nested_tuple_copy() == "(1, [2]) (1, [2, 3])"

def test_copy_06_set_copy_independent():
    assert X.copy_06_set_copy_independent() == "[1, 2] [1, 2, 3]"

def test_copy_07_copy_module_copy_vs_deepcopy():
    assert X.copy_07_copy_module_copy_vs_deepcopy() == "9 1"

def test_copy_08_tuple_of_lists_shallow():
    assert X.copy_08_tuple_of_lists_shallow() == "([1, 5], [2]) ([1, 5], [2])"

def test_copy_09_list_of_dicts_deepcopy():
    assert X.copy_09_list_of_dicts_deepcopy() == "[{'x': 1}, {'y': 2}] [{'x': 99}, {'y': 2}]"

def test_copy_10_nested_defaultdict_shallow():
    assert X.copy_10_nested_defaultdict_shallow() == "[1, 2] [1, 2]"


# 4) Pass-by-Object-Reference & Function Args — (x10)

def test_pass_01_int_param():
    assert X.pass_01_int_param() == ["inside: 11", "outside: 10"]

def test_pass_02_list_param_mutate():
    assert X.pass_02_list_param_mutate() == ["inside: [1, 2, 3, 4]", "outside: [1, 2, 3, 4]"]

def test_pass_03_rebind_list_param():
    assert X.pass_03_rebind_list_param() == ["inside: [9]", "outside: [1, 2]"]

def test_pass_04_defaults_eval_once():
    assert X.pass_04_defaults_eval_once() is True

def test_pass_05_kwargs_binding():
    assert X.pass_05_kwargs_binding() == 12

def test_pass_06_args_collect():
    assert X.pass_06_args_collect() == "(1, 2, 3)"

def test_pass_07_kwargs_collect():
    assert X.pass_07_kwargs_collect() == "[('a', 1), ('z', 3)]"

def test_pass_08_args_kwargs_mix():
    assert X.pass_08_args_kwargs_mix() == "1 2 [('x', 9)]"

def test_pass_09_mutable_default_pitfall():
    assert X.pass_09_mutable_default_pitfall() == ["[1]", "[1, 2]"]

def test_pass_10_safe_default_pattern():
    assert X.pass_10_safe_default_pattern() == ["[1]", "[2]"]


# 5) Loops, else & break — (x10)

def test_loop_01_else_no_break():
    assert X.loop_01_else_no_break() == ["0", "1", "2", "done"]

def test_loop_02_else_with_break():
    assert X.loop_02_else_with_break() == ["0", "break at 1"]

def test_loop_03_nested_breaks():
    assert X.loop_03_nested_breaks() == [
        "0 0", "break inner", "outer continues",
        "1 0", "break inner", "outer continues"
    ]

def test_loop_04_while_truthy():
    assert X.loop_04_while_truthy() == ["3", "2", "1", "[]"]

def test_loop_05_for_iterable_snapshot():
    assert X.loop_05_for_iterable_snapshot() == ["1", "2", "3", "[1, 2, 3, 4]"]

def test_loop_06_range_rebind_inside():
    assert X.loop_06_range_rebind_inside() == ["0", "1", "2"]

def test_loop_07_continue_skips_else():
    assert X.loop_07_continue_skips_else() == ["0", "continue at 1", "2", "done"]

def test_loop_08_break_in_while_else():
    assert X.loop_08_break_in_while_else() == ["3", "break!"]

def test_loop_09_iter_mutate_delete():
    assert X.loop_09_iter_mutate_delete() == ["0", "2", "[1, 3]"]

def test_loop_10_enumerate_safe():
    assert X.loop_10_enumerate_safe() == ["0 10", "1 20", "2 30", "[10, 30]"]


# 6) Conditionals & Truthiness & Short-Circuit (x10)

def test_cond_01_and_or_order():
    assert X.cond_01_and_or_order() == ["7", "2"]

def test_cond_02_chain_compare():
    assert X.cond_02_chain_compare() == ["peek 2", "True"]

def test_cond_03_truthiness_values():
    assert X.cond_03_truthiness_values() == ["False", "True", "False"]

def test_cond_04_none_identity():
    assert X.cond_04_none_identity() == "True True"

def test_cond_05_bool_ops_return_operand():
    assert X.cond_05_bool_ops_return_operand() == ["[1]", "42"]

def test_cond_06_ternary_binding():
    assert X.cond_06_ternary_binding() == "A"

def test_cond_07_in_operator_strings():
    assert X.cond_07_in_operator_strings() == "True False"

def test_cond_08_any_all_shortcircuit():
    assert X.cond_08_any_all_shortcircuit() == ["check 0", "check 0", "check 3", "True"]

def test_cond_09_bool_int_arithmetic():
    assert X.cond_09_bool_int_arithmetic() == "2 5"

def test_cond_10_dict_key_truthiness():
    assert X.cond_10_dict_key_truthiness() == "True False"