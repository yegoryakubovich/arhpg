from django.contrib import admin

from admin_web.admin import admin_site
from admin_web.models import Faq


@admin.register(Faq, site=admin_site)
class FaqAdmin(admin.ModelAdmin):
    fields = ("question", "answer_button")
    list_display = ("type", "question", "answer_button")
    list_display_links = ("type", "question", "answer_button")
    list_filter = ("type",)

    def has_add_permission(self, request):
        return False

