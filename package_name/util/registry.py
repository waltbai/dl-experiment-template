"""Simple registry class."""


class Registry:
    """Registry class."""

    def __init__(self):
        self._elements = {}

    def register(self, key):
        """Register an element with key."""
        def _decorator_register(value):
            if key in self._elements:
                # raise KeyError(f"Duplicate key '{key}'!")
                pass
            else:
                self._elements.setdefault(key, value)
                return value
        return _decorator_register

    def get(self, key):
        """Get an element from registry."""
        return self._elements[key]
