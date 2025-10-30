# Miscellaneous & Conceptual Practice — Guess the Output 

# ======================================================
# RETURN CONVENTIONS:
# • Do NOT print. Return what the program would have printed.
# • If multiple lines would print, return a list[str] in order.
# • If the code raises an error, return -1.
# • If it computes a value, return that value directly (int, tuple, etc.).
# ======================================================


# So for this one you just answer the question

from __future__ import annotations

# ======================================================
# 1) Variable Scope & Namespaces — Guess the Output (x10)
# ======================================================

def scope_01_shadowing() -> tuple[int, int]:
    """
    Local vs global shadowing — return (inside_x, outside_x). Do not print.

    Task:
        The code below runs and prints two lines. **Instead of printing**, return a tuple
        `(inside_val, outside_val)` representing the values that would be printed for `x`
        inside the function and outside at module scope (in that order).

    Prompt:
        >>> x = 5
        >>> def f():
        ...     x = 10
        ...     print("inside:", x)
        >>> f()
        >>> print("outside:", x)
    """
    raise ValueError("TODO: implement scope_01_shadowing")


def scope_02_unbound_local() -> None:
    """
    Assignment makes x local;

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> x = 7
        >>> def g():
        ...     print(x)
        ...     x = 9
        >>> g()
    """
    raise ValueError("TODO: implement scope_02_unbound_local")


def scope_03_global_stmt() -> None:
    """
    Use of 'global' rebinding affects module-level variable; return printed lines as list[str].

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> x = 3
        >>> def h():
        ...     global x
        ...     x = 99
        ...     print("set x to", x)
        >>> h()
        >>> print("after:", x)
    """
    raise ValueError("TODO: implement scope_03_global_stmt")


def scope_04_nonlocal_chain() -> None:
    """
    'nonlocal' modifies nearest enclosing function variable; return printed lines as list[str].

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> def outer():
        ...     x = 1
        ...     def inner():
        ...         nonlocal x
        ...         x += 2
        ...         print("inner:", x)
        ...     inner()
        ...     print("outer:", x)
        >>> outer()
    """
    raise ValueError("TODO: implement scope_04_nonlocal_chain")


def scope_05_comp_scope() -> None:
    """
    Comprehension variable is local; outer x unchanged. Return printed lines as list[str].

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> x = 100
        >>> y = [x for x in range(3)]
        >>> print("y:", y)
        >>> print("x:", x)
    """
    raise ValueError("TODO: implement scope_05_comp_scope")


def scope_06_for_var_leaks() -> None:
    """
    Loop variable remains bound after loop; return printed value.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> for k in range(2):
        ...     pass
        >>> print(k)
    """
    raise ValueError("TODO: implement scope_06_for_var_leaks")


def scope_07_del_name() -> None:
    """
    'del' removes name binding, not object; return printed lines as list[str].

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> x = [1]
        >>> y = x
        >>> del x
        >>> print(y)
        >>> 'x' in locals()
    """
    raise ValueError("TODO: implement scope_07_del_name")


def scope_08_default_capture_time() -> None:
    """
    Default parameter captures value at function definition; return printed value.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> y = 10
        >>> def f(x=y):
        ...     print(x)
        >>> y = 20
        >>> f()
    """
    raise ValueError("TODO: implement scope_08_default_capture_time")


def scope_09_nested_shadowing() -> None:
    """
    Nested local variables shadow outer ones; return all printed lines as list[str].

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> x = 1
        >>> def outer():
        ...     x = 2
        ...     def inner():
        ...         x = 3
        ...         print('inner:', x)
        ...     inner()
        ...     print('outer:', x)
        >>> outer()
        >>> print('global:', x)
    """
    raise ValueError("TODO: implement scope_09_nested_shadowing")


def scope_10_class_scope_lookup() -> None:
    """
    Class body executes at definition; method name lookup at runtime. Return printed lines as list[str].

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> X = 1
        >>> class C:
        ...     X = 2
        ...     print('class body X =', X)
        ...     def show(self):
        ...         print(X, self.X, C.X)
        >>> C().show()
    """
    raise ValueError("TODO: implement scope_10_class_scope_lookup")


# ======================================
# 2) Mutability & Immutability (x10)
# ======================================

def mut_01_list_vs_tuple() -> None:
    """
    Lists mutate; tuples don't.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> lst = [1, 2, 3]
        >>> tup = (1, 2, 3)
        >>> lst[1] = 99
        >>> print(lst)
        >>> print(tup)
    """
    raise ValueError("TODO: implement mut_01_list_vs_tuple")


def mut_02_string_methods() -> None:
    """
    Strings are immutable; methods return new strings.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> s = "hello"
        >>> t = s.upper()
        >>> print("t:", t)
        >>> print("s:", s)
    """
    raise ValueError("TODO: implement mut_02_string_methods")


def mut_03_aliasing() -> None:
    """
    Aliasing two names to same list object.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> a = [1, 2]
        >>> b = a
        >>> b.append(3)
        >>> print(a, b, a is b)
    """
    raise ValueError("TODO: implement mut_03_aliasing")


def mut_04_tuple_with_list() -> None:
    """
    Tuples are immutable but may contain mutable elements.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> t = (1, [2, 3])
        >>> t[1].append(4)
        >>> print(t)
    """
    raise ValueError("TODO: implement mut_04_tuple_with_list")


def mut_05_frozenset_behavior() -> None:
    """
    frozenset is immutable; set is mutable.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> s = {1, 2}
        >>> fs = frozenset({1, 2})
        >>> s.add(3)
        >>> print(sorted(s))
        >>> print(sorted(fs))
    """
    raise ValueError("TODO: implement mut_05_frozenset_behavior")


def mut_06_bytes_vs_bytearray() -> None:
    """
    bytes is immutable; bytearray is mutable.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> b = b"abc"
        >>> ba = bytearray(b)
        >>> try:
        ...     b[0] = 100
        ... except TypeError as e:
        ...     print(type(e).__name__)
        >>> ba[0] = 100
        >>> print(bytes(ba))
    """
    raise ValueError("TODO: implement mut_06_bytes_vs_bytearray")


def mut_07_dict_alias_mutation() -> None:
    """
    Dict aliasing mutates both names.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> d1 = {"x": 1}
        >>> d2 = d1
        >>> d2["y"] = 2
        >>> print(d1)
    """
    raise ValueError("TODO: implement mut_07_dict_alias_mutation")


def mut_08_tuple_concat_new_obj() -> None:
    """
    Tuple concatenation creates a new object.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> t1 = (1, 2)
        >>> t2 = t1 + (3,)
        >>> print(t1, t2, t1 is t2)
    """
    raise ValueError("TODO: implement mut_08_tuple_concat_new_obj")


def mut_09_list_copy_method() -> None:
    """
    list.copy() is shallow.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> a = [[1], [2]]
        >>> b = a.copy()
        >>> b[0].append(9)
        >>> print(a, b, a is b)
    """
    raise ValueError("TODO: implement mut_09_list_copy_method")


def mut_10_str_replace_creates_new() -> None:
    """
    str.replace returns new string.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> s = "banana"
        >>> t = s.replace("a", "o")
        >>> print(t)
        >>> print(s)
    """
    raise ValueError("TODO: implement mut_10_str_replace_creates_new")


# ==================================
# 3) Shallow vs Deep Copy (x10)
# ==================================

def copy_01_shallow_top() -> None:
    """
    Shallow copy clones top level only.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> import copy
        >>> a = [[1, 2], [3, 4]]
        >>> b = copy.copy(a)
        >>> b[0][0] = 99
        >>> print(a)
        >>> print(b)
    """
    raise ValueError("TODO: implement copy_01_shallow_top")


def copy_02_deepcopy() -> None:
    """
    Deep copy clones nested structures.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> import copy
        >>> a = [[1, 2], [3, 4]]
        >>> b = copy.deepcopy(a)
        >>> b[0][0] = 99
        >>> print(a)
        >>> print(b)
    """
    raise ValueError("TODO: implement copy_02_deepcopy")


def copy_03_slice_copy() -> None:
    """
    list slicing makes a shallow copy of the list.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> a = [[1], [2]]
        >>> b = a[:]
        >>> b[0].append(9)
        >>> print(a, b, a is b)
    """
    raise ValueError("TODO: implement copy_03_slice_copy")


def copy_04_dict_copy_vs_update() -> None:
    """
    dict.copy() shallow copies; nested values alias.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> d1 = {"x": [1]}
        >>> d2 = d1.copy()
        >>> d2["x"].append(2)
        >>> print(d1, d2)
    """
    raise ValueError("TODO: implement copy_04_dict_copy_vs_update")


def copy_05_nested_tuple_copy() -> None:
    """
    deepcopy also clones lists inside tuples.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> import copy
        >>> t1 = (1, [2])
        >>> t2 = copy.deepcopy(t1)
        >>> t2[1].append(3)
        >>> print(t1, t2)
    """
    raise ValueError("TODO: implement copy_05_nested_tuple_copy")


def copy_06_set_copy_independent() -> None:
    """
    set.copy makes independent top-level set.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> s1 = {1, 2}
        >>> s2 = s1.copy()
        >>> s2.add(3)
        >>> print(sorted(s1), sorted(s2))
    """
    raise ValueError("TODO: implement copy_06_set_copy_independent")


def copy_07_copy_module_copy_vs_deepcopy() -> None:
    """
    copy vs deepcopy with nested dict.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> import copy
        >>> d = {"a": {"b": 1}}
        >>> c1 = copy.copy(d)
        >>> c2 = copy.deepcopy(d)
        >>> c1["a"]["b"] = 9
        >>> print(d["a"]["b"], c2["a"]["b"])  # d and c1 changed; c2 isolated
    """
    raise ValueError("TODO: implement copy_07_copy_module_copy_vs_deepcopy")


def copy_08_tuple_of_lists_shallow() -> None:
    """
    Shallow copy of tuple only copies tuple container.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> import copy
        >>> t = ([1], [2])
        >>> t2 = copy.copy(t)
        >>> t2[0].append(5)
        >>> print(t, t2)
    """
    raise ValueError("TODO: implement copy_08_tuple_of_lists_shallow")


def copy_09_list_of_dicts_deepcopy() -> None:
    """
    Deepcopy isolates nested dicts in list.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> import copy
        >>> L = [{"x": 1}, {"y": 2}]
        >>> M = copy.deepcopy(L)
        >>> M[0]["x"] = 99
        >>> print(L, M)
    """
    raise ValueError("TODO: implement copy_09_list_of_dicts_deepcopy")


def copy_10_nested_defaultdict_shallow() -> None:
    """
    Shallow copy of defaultdict shares default factory & nested values unless deepcopied.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> import copy, collections
        >>> d = collections.defaultdict(list)
        >>> d['a'].append(1)
        >>> e = copy.copy(d)
        >>> e['a'].append(2)
        >>> print(d['a'], e['a'])
    """
    raise ValueError("TODO: implement copy_10_nested_defaultdict_shallow")


# ============================================================
# 4) Pass-by-Object-Reference & Function Args — (x10)
# ============================================================

def pass_01_int_param() -> None:
    """
    Integers are immutable; rebinding inside function doesn't affect caller.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> def bump(n):
        ...     n += 1
        ...     print("inside:", n)
        >>> x = 10
        >>> bump(x)
        >>> print("outside:", x)
    """
    raise ValueError("TODO: implement pass_01_int_param")


def pass_02_list_param_mutate() -> None:
    """
    Mutating a list argument affects the caller's object.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> def touch(lst):
        ...     lst.append(4)
        ...     print("inside:", lst)
        >>> a = [1, 2, 3]
        >>> touch(a)
        >>> print("outside:", a)
    """
    raise ValueError("TODO: implement pass_02_list_param_mutate")


def pass_03_rebind_list_param() -> None:
    """
    Rebinding the parameter name doesn't affect caller.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> def replace(lst):
        ...     lst = [9]
        ...     print("inside:", lst)
        >>> a = [1, 2]
        >>> replace(a)
        >>> print("outside:", a)
    """
    raise ValueError("TODO: implement pass_03_rebind_list_param")


def pass_04_defaults_eval_once() -> None:
    """
    Default arguments are evaluated at function definition time.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> import time
        >>> t0 = time.time()
        >>> def stamp(t=t0):
        ...     print(t == t0)
        >>> time.sleep(0.01)
        >>> stamp()
    """
    raise ValueError("TODO: implement pass_04_defaults_eval_once")


def pass_05_kwargs_binding() -> None:
    """
    Keyword arguments bind by name; order doesn't matter.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> def area(w, h):
        ...     print(w * h)
        >>> area(h=3, w=4)
    """
    raise ValueError("TODO: implement pass_05_kwargs_binding")


def pass_06_args_collect() -> None:
    """
    *args collects positionals.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> def f(*args):
        ...     print(args)
        >>> f(1, 2, 3)
    """
    raise ValueError("TODO: implement pass_06_args_collect")


def pass_07_kwargs_collect() -> None:
    """
    **kwargs collects keywords.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> def g(**kwargs):
        ...     print(sorted(kwargs.items()))
        >>> g(z=3, a=1)
    """
    raise ValueError("TODO: implement pass_07_kwargs_collect")


def pass_08_args_kwargs_mix() -> None:
    """
    Mixing positionals and keywords.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> def h(a, b=0, **kw):
        ...     print(a, b, sorted(kw.items()))
        >>> h(1, **{"b": 2, "x": 9})
    """
    raise ValueError("TODO: implement pass_08_args_kwargs_mix")


def pass_09_mutable_default_pitfall() -> None:
    """
    Mutable default persists across calls.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> def push(x, acc=[]):
        ...     acc.append(x)
        ...     print(acc)
        >>> push(1); push(2)
    """
    raise ValueError("TODO: implement pass_09_mutable_default_pitfall")


def pass_10_safe_default_pattern() -> None:
    """
    Use None + new list inside.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> def push(x, acc=None):
        ...     if acc is None:
        ...         acc = []
        ...     acc.append(x)
        ...     print(acc)
        >>> push(1); push(2)
    """
    raise ValueError("TODO: implement pass_10_safe_default_pattern")


# =====================================
# 5) Loops, else & break — (x10)
# =====================================

def loop_01_else_no_break() -> None:
    """
    'else' executes when loop completes without 'break'.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> for i in range(3):
        ...     print(i)
        ... else:
        ...     print("done")
    """
    raise ValueError("TODO: implement loop_01_else_no_break")


def loop_02_else_with_break() -> None:
    """
    'else' skipped if 'break' executed.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> for i in range(3):
        ...     if i == 1:
        ...         print("break at", i)
        ...         break
        ...     print(i)
        ... else:
        ...     print("done")
    """
    raise ValueError("TODO: implement loop_02_else_with_break")


def loop_03_nested_breaks() -> None:
    """
    Break only exits innermost loop.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> for i in range(2):
        ...     for j in range(3):
        ...         if j == 1:
        ...             print("break inner")
        ...             break
        ...         print(i, j)
        ...     print("outer continues")
    """
    raise ValueError("TODO: implement loop_03_nested_breaks")


def loop_04_while_truthy() -> None:
    """
    while consumes and mutates list via pop.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> a = [1, 2, 3]
        >>> while a:
        ...     print(a.pop())
        >>> print(a)
    """
    raise ValueError("TODO: implement loop_04_while_truthy")


def loop_05_for_iterable_snapshot() -> None:
    """
    For iterates over snapshot of indices; appending inside doesn't extend current iteration.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> a = [1, 2, 3]
        >>> for x in a:
        ...     print(x)
        ...     if x == 1:
        ...         a.append(4)
        >>> print(a)
    """
    raise ValueError("TODO: implement loop_05_for_iterable_snapshot")


def loop_06_range_rebind_inside() -> None:
    """
    Reassigning loop variable doesn't affect iteration sequence.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> for i in range(3):
        ...     print(i)
        ...     i = 100
    """
    raise ValueError("TODO: implement loop_06_range_rebind_inside")


def loop_07_continue_skips_else() -> None:
    """
    continue doesn't skip else; only break skips else.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> for i in range(3):
        ...     if i == 1:
        ...         print('continue at', i)
        ...         continue
        ...     print(i)
        ... else:
        ...     print('done')
    """
    raise ValueError("TODO: implement loop_07_continue_skips_else")


def loop_08_break_in_while_else() -> None:
    """
    while-else executes only if loop not broken.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> n = 3
        >>> while n:
        ...     if n == 2:
        ...         print('break!')
        ...         break
        ...     print(n)
        ...     n -= 1
        ...
        ...
        >>> else:
        ...     print('done')
    """
    raise ValueError("TODO: implement loop_08_break_in_while_else")


def loop_09_iter_mutate_delete() -> None:
    """
    Removing while iterating by index can skip elements.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> a = [0, 1, 2, 3]
        >>> i = 0
        >>> while i < len(a):
        ...     print(a[i])
        ...     del a[i]
        ...     i += 1
        >>> print(a)
    """
    raise ValueError("TODO: implement loop_09_iter_mutate_delete")


def loop_10_enumerate_safe() -> None:
    """
    enumerate + copy to avoid mutation issues.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> a = [10, 20, 30]
        >>> for i, x in enumerate(a[:]):
        ...     print(i, x)
        ...     if x == 20:
        ...         a.remove(20)
        >>> print(a)
    """
    raise ValueError("TODO: implement loop_10_enumerate_safe")


# ===============================================
# 6) Conditionals & Truthiness & Short-Circuit (x10)
# ===============================================

def cond_01_and_or_order() -> None:
    """
    'and' / 'or' short-circuit with operand return.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> print(0 and 5 or 7)
        >>> print(1 and 0 or 2)
    """
    raise ValueError("TODO: implement cond_01_and_or_order")


def cond_02_chain_compare() -> None:
    """
    Chained comparisons don't evaluate middle twice.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> def peek(x):
        ...     print("peek", x)
        ...     return x
        >>> print(1 < peek(2) < 3)
    """
    raise ValueError("TODO: implement cond_02_chain_compare")


def cond_03_truthiness_values() -> None:
    """
    Truthiness of empty / non-empty structures.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> print(bool("")) ; print(bool([0])) ; print(bool([]))
    """
    raise ValueError("TODO: implement cond_03_truthiness_values")


def cond_04_none_identity() -> None:
    """
    'is' checks identity, not equality.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> a = None
        >>> b = None
        >>> print(a is b, a == b)
    """
    raise ValueError("TODO: implement cond_04_none_identity")


def cond_05_bool_ops_return_operand() -> None:
    """
    'and' returns first falsy else last; 'or' returns first truthy.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> print([] or [1])
        >>> print([0] and 42)
    """
    raise ValueError("TODO: implement cond_05_bool_ops_return_operand")


def cond_06_ternary_binding() -> None:
    """
    Ternary operator associates right-to-left only within single expression.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> a = 1; b = 2
        >>> print('A' if a < b else 'B' if b < 0 else 'C')
    """
    raise ValueError("TODO: implement cond_06_ternary_binding")


def cond_07_in_operator_strings() -> None:
    """
    'in' checks substring membership for strings.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> print('ana' in 'banana', 'x' in 'banana')
    """
    raise ValueError("TODO: implement cond_07_in_operator_strings")


def cond_08_any_all_shortcircuit() -> None:
    """
    any/all short-circuit.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> def show(x):
        ...     print('check', x)
        ...     return bool(x)
        >>> print(any(show(x) for x in [0, 0, 3, 0]))
    """
    raise ValueError("TODO: implement cond_08_any_all_shortcircuit")


def cond_09_bool_int_arithmetic() -> None:
    """
    True == 1, False == 0 under arithmetic.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> print(True + True + False, True * 5)
    """
    raise ValueError("TODO: implement cond_09_bool_int_arithmetic")


def cond_10_dict_key_truthiness() -> None:
    """
    Empty string key is allowed and falsy; membership uses keys.

    Task:
        Predict exactly what will be printed by running the Prompt. Write the output lines in order.

    Prompt:
        >>> d = {'': 1, 'a': 2}
    
        >>> print('' in d, bool(''))
    """
    raise ValueError("TODO: implement cond_10_dict_key_truthiness")