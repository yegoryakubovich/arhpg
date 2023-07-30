from django.contrib import admin

from admin_web.admin import admin_site
from admin_web.models import NotificationUser


@admin.register(NotificationUser, site=admin_site)
class NotificationUserAdmin(admin.ModelAdmin):
    list_display = ("id", "notification", "user")
