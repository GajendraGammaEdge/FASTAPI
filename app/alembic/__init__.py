# models/__init__.py
import os
import glob
import importlib

# Get all .py files in this folder (except __init__.py)
modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
for module in modules:
    module_name = os.path.basename(module)[:-3]
    if module_name != "__init__":
        importlib.import_module(f"{__name__}.{module_name}")
