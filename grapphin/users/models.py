"""
User models.
"""

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User model.
    """

    __prefix__ = "users"

    def __str__(self):
        return self.email
