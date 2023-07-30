from django.contrib import admin

from admin_web.admin import admin_site
from admin_web.models import Setting


@admin.register(Setting, site=admin_site)
class SettingAdmin(admin.ModelAdmin):
    list_display = ("id", "key", "value")
    list_editable = ("value",)
    readonly_fields = ("id", "key")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
