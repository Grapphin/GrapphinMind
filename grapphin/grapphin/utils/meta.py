"""
Meta (programming) utils.
"""

class classproperty: # pylint: disable=invalid-name
    """
    Descriptor for a class property.
    """

    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, caller):
        return self.getter(caller)
