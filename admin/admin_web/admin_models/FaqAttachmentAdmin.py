from django.contrib import admin

from admin_web.admin import admin_site
from admin_web.models import FaqAttachment


@admin.register(FaqAttachment, site=admin_site)
class FaqAttachmentAdmin(admin.ModelAdmin):
    list_display = ("id", "faq", "type", "value")
    list_filter = ("type",)
