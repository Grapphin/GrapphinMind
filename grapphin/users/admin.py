"""
Django admin definition.
"""

from django.contrib import admin
from users import models as users


admin.site.register(users.User)
