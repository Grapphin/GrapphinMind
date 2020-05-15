"""
Model mixins.
"""

from django.db import models
from django.utils import timezone


class GModel(models.Model):
    """
    Base GModel.
    """

    class Meta:
        abstract = True


class HistoricMixin(models.Model):
    """
    Provides the `created` and `modified` fields.
    """

    class Meta:
        abstract = True


    created = models.DateTimeField(
        default=timezone.now,
        null=False,
        blank=True,
    )

    modified = models.DateTimeField(
        default=timezone.now,
        null=False,
        blank=True,
    )


class OwnedMixin(models.Model):
    """
    Provides the `owner` and `public` fields.
    """

    class Meta:
        abstract = True

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    public = models.BooleanField(
        default=False,
    )


def q__owned_or_public(user_id):
    """
    Generates a Q object to check whether
    the object is owned or public.
    """

    query = models.Q(public=True) | models.Q(owner_id=user_id)

    return query
