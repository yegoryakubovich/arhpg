from django.contrib import admin

from admin_web.admin import admin_site
from admin_web.models import NotificationReport


@admin.register(NotificationReport, site=admin_site)
class NotificationReportAdmin(admin.ModelAdmin):
    list_display = ("id", "notification", "user", "state", "datetime")
    list_filter = ("state",)
