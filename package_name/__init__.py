import pkgutil

from package_name.util.registry import Registry


# Initialize a registry
CLASSES = Registry()
# Pre-load all submodules to register
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    _module = loader.find_module(module_name).load_module(module_name)
