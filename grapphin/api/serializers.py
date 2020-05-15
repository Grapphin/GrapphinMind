"""
Grapphin serializers.
"""

from django.utils.functional import cached_property
from rest_framework.serializers import ModelSerializer

from grapphin.utils.meta import classproperty


class GSerializerMixin:
    """
    Pho base serializer mixin.
    """

    @cached_property
    def request(self):
        """
        Wrapper over `self.context.get("request")`.
        """

        return self.context.get("request")


class GModelSer(
    ModelSerializer,
    GSerializerMixin,
):
    """
    Pho model serializer.
    """

    @classproperty
    def model(self):
        """
        Reference to cls.Meta.model.
        """

        try:
            return getattr(self, "Meta").model

        except AttributeError:
            raise Exception("The serializer doesn't define a complete Meta class.")
