import os
import glob
import importlib

# Automatically import all model files in this folder
modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
for module in modules:
    name = os.path.basename(module)[:-3]
    if name != "__init__":
        importlib.import_module(f"{__name__}.{name}")
