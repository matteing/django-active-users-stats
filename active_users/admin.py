"""Admin classes for the active_users app."""
from django.contrib import admin

from . import models


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['day', 'count', 'user', 'user__email', 'last_active']
    search_fields = ['user__email']
    raw_id_fields = ['user']

    def user__email(self, obj):
        return "user@deleted.null" if not obj.user else obj.user.email


admin.site.register(models.Activity, ActivityAdmin)
