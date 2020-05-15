"""
REST Serializers for GrapphinMind.
"""

from api.serializers import GModelSer
from mind import models as mind


class GTreeSer(GModelSer):
    """
    Serializer for a GTree.
    """

    class Meta:
        model = mind.GTree
        fields = (
            "id",
            "name",
            "description",
        )


class GNodeSer(GModelSer):
    """
    Serializer for a GNode.
    """

    class Meta:
        model = mind.GNode
        fields = (
            "id",
            "name",
            "owner",
            "owner",
            "public",
            "inbound_nodes",
            "outbound_nodes",
        )


class GContentSer(GModelSer):
    """
    Serializer for a GContent.
    """

    class Meta:
        model = mind.GContent
        fields = (
            "id",
            "node",
            "kind",
            "content",
        )
