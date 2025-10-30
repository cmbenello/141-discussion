# tests/conftest.py
import os, sys, types, pytest

# 1) Put repo root on sys.path so `import problems` works.
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# 2) Optional: run tests against solutions instead of stubs when USE_SOLUTIONS=1.
USE_SOLUTIONS = os.getenv("USE_SOLUTIONS", "").lower() in {"1", "true", "yes", "on"}

def _alias_module(sol_mod, target_qualified_name: str):
    """
    Make pytest import `target_qualified_name` resolve to `sol_mod`.
    Example: target_qualified_name='problems.assessement'
    """
    alias = types.ModuleType(target_qualified_name)
    for name in dir(sol_mod):
        try:
            setattr(alias, name, getattr(sol_mod, name))
        except Exception:
            pass
    sys.modules[target_qualified_name] = alias


if USE_SOLUTIONS:
    # assessment (keep misspelling compatibility: 'assessement')
    try:
        import solutions.assessment_sols as _SOL_A
        _alias_module(_SOL_A, "problems.assessement")
    except Exception:
        pass

    # expressions
    try:
        import solutions.expressions_sols as _SOL_E
        _alias_module(_SOL_E, "problems.expressions")
    except Exception:
        pass

    # strings_list
    try:
        import solutions.strings_list_sols as _SOL_SL
        _alias_module(_SOL_SL, "problems.strings_list")
    except Exception:
        pass

# 3) Keep any module-level counters tidy across tests.
@pytest.fixture(autouse=True)
def _reset_global_counter():
    # handle both direct import and aliased solutions
    for mod_name in ("problems.assessement", "solutions.assessment_sols"):
        mod = sys.modules.get(mod_name)
        if mod and hasattr(mod, "GLOBAL_COUNTER"):
            mod.GLOBAL_COUNTER = 0
    yield
    for mod_name in ("problems.assessement", "solutions.assessment_sols"):
        mod = sys.modules.get(mod_name)
        if mod and hasattr(mod, "GLOBAL_COUNTER"):
            mod.GLOBAL_COUNTER = 0