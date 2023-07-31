from django.contrib import admin

from admin_web.admin import admin_site
from admin_web.models import Faq, FaqAttachment


class SessionTaskInline(admin.TabularInline):
    model = FaqAttachment
    extra = 0
    fields = ("type", "value")
    readonly_fields = ("type",)

    show_change_link = False

    def has_add_permission(self, request, obj):
        return False


@admin.register(Faq, site=admin_site)
class FaqAdmin(admin.ModelAdmin):
    fields = ("question", "answer_button")
    list_display = ("type", "question", "answer_button")
    list_display_links = ("type", "question", "answer_button")
    list_filter = ("type",)
    inlines = [SessionTaskInline]

    def has_add_permission(self, request):
        return False

