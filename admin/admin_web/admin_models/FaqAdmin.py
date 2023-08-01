from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.views import View

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
    list_display = ("type", "question", "answer_button", "button_priority")
    list_display_links = ("type", "question", "answer_button")
    inlines = [SessionTaskInline]

    def has_add_permission(self, request):
        return False

    @admin.display(description="Приоритетность")
    def button_priority(self, model: Faq):
        return format_html(" ".join([
            f'<a href="/admin/admin_web/faq_priority_up?faq_id={model.id}"><input type="button" value="↑"></a>',
            f'<a href="/321"><input type="button" value="↓"></a>'
        ]))

    def get_queryset(self, request):
        queryset = Faq.objects.order_by('-priority').all()
        return queryset


class PriorityUpView(View):
    path_link = "admin_web/faq_priority_up"

    def get(self, request):
        faq_id = int(request.GET.get("faq_id"))
        faq = Faq.objects.filter(id=faq_id).first()
        faq_up = Faq.objects.filter(priority=faq.priority + 1).first()
        if not faq_up:
            messages.error("Error")
            return HttpResponseRedirect("/admin/admin_web/faq/")

        faq.priority += 1
        faq_up -= 1

        faq.save()
        faq_up.save()
        return HttpResponseRedirect("/admin/admin_web/faq/")
