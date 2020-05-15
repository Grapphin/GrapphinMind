"""
Grapphin viewsets.
"""

from django.conf import settings
from rest_framework.viewsets import ModelViewSet

from grapphin.utils.meta import classproperty


class GViewMixin:
    """
    Grapphin base viewset mixin.
    """


class GModelView(
    ModelViewSet,
    GViewMixin,
):
    """
    Grapphin model view set.
    """

    @classproperty
    def queryset(self):
        """
        Generates a reference to the model queryset
        based on the serializer's model.
        """

        try:
            return getattr(self, "serializer_class").model.objects.all()

        except AttributeError:
            raise Exception("The model viewset isn't properly initialised.")


    def dispatch(self, request, *args, **kwargs):
        """
        Adds custom headers to API responses.
        """

        response = super().dispatch(request, *args, **kwargs)

        if settings.DEBUG:
            response["Access-Control-Allow-Origin"] = request.META.get("HTTP_ORIGIN", "*")
        else:
            response["Access-Control-Allow-Origin"] = settings.WEB_APP_ORIGIN

        response["Access-Control-Allow-Credentials"] = "true"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        response["Access-Control-Allow-Methods"] = ",".join([
            "GET",
            "POST",
            "PUT",
            "DELETE",
            "HEAD",
            "OPTIONS",
        ])

        return response
