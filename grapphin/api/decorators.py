"""
REST decorators.
"""

from rest_framework.decorators import action as rest_action


def action(method, path, detail=False):
    """
    Wrapper over rest_framework.decorators.action.
    """

    return rest_action(methods=[method], detail=detail, url_path=path, url_name=path)
