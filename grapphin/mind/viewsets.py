"""
Grapphin viewsets.
"""

from api.viewsets import GModelView
from grapphin.models import q__owned_or_public
from mind.serializers import (
    GTreeSer,
    GNodeSer,
    GContentSer,
)


class GTreeView(GModelView):
    """
    Media Category viewset.
    """

    serializer_class = GTreeSer

    def get_queryset(self):
        owned_or_public = q__owned_or_public(self.request.user.id)
        qs = super().get_queryset()
        qs = qs.filter(owned_or_public)

        return qs


class GNodeView(GModelView):
    """
    Media Category viewset.
    """

    serializer_class = GNodeSer

    def get_queryset(self):
        owned_or_public = q__owned_or_public(self.request.user.id)
        qs = super().get_queryset()
        qs = qs.filter(owned_or_public)

        return qs


class GContentView(GModelView):
    """
    Media Leaf viewset.
    """

    serializer_class = GContentSer
