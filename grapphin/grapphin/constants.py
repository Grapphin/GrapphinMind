"""
Grapphin constants.
"""


def define(choices, value, label):
    """
    Appends a constant to the choices.
    """

    choices.append((value, label))
    return value


class NodeContent:
    """
    Node content type.
    """

    choices = []

    TEXT = define(choices, "TEXT", "Text")
    IMAGE = define(choices, "IMAGE", "Image")
    VIDEO = define(choices, "VIDEO", "Video")
    SOUND = define(choices, "SOUND", "Sound")
