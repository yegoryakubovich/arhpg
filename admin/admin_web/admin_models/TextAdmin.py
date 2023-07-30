from django.contrib import admin

from admin_web.admin import admin_site
from admin_web.models import Text


@admin.register(Text, site=admin_site)
class TextAdmin(admin.ModelAdmin):
    fields = ("value",)
    list_display = ("key", "value")
    list_filter = ("category",)
    list_editable = ("value",)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
