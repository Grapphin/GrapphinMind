"""
Grapphin REST API routers.
"""

from rest_framework.routers import DefaultRouter


class GraphRouter(DefaultRouter):
    """
    Grapphin REST API router.
    """

    def include(self, viewset, *args, prefix=None, **kwargs):
        """
        Registration shortcut.
        """

        if prefix is None:
            prefix = viewset.serializer_class.model.__prefix__

        return self.register(prefix, viewset, *args, **kwargs)
