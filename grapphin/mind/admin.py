"""
Django admin site.
"""

from django.contrib import admin

from mind import models as mind


admin.site.register(mind.GTree)
admin.site.register(mind.GNode)
admin.site.register(mind.GContent)
admin.site.register(mind.GBranch)
