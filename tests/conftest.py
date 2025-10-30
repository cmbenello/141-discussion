# tests/conftest.py
import os, sys, types, pytest

# 1) Put repo root on sys.path so `import problems` works.
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# # 2) (Optional) Solution-check alias: run tests against solutions.
# try:
#     import solutions.assessment_sols as SOL
# except Exception:
#     SOL = None

# if SOL is not None:
#     alias = types.ModuleType("problems.assessement")  # keep your current misspelling
#     for name in dir(SOL):
#         setattr(alias, name, getattr(SOL, name))
#     sys.modules["problems.assessement"] = alias

# 3) Keep any module-level counters tidy across tests.
@pytest.fixture(autouse=True)
def _reset_global_counter():
    mod = sys.modules.get("problems.assessement")
    if mod and hasattr(mod, "GLOBAL_COUNTER"):
        mod.GLOBAL_COUNTER = 0
    yield
    if mod and hasattr(mod, "GLOBAL_COUNTER"):
        mod.GLOBAL_COUNTER = 0