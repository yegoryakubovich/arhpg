from django.contrib import admin
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.contrib.admin.views.decorators import staff_member_required

from admin_web.admin import admin_site
from admin_web.models import Notification
from admin_web.models.notification import NotificationState


@admin.action(description="Выгрузить логи отправленных уведомлений")
def export_competed(model_admin: admin.ModelAdmin, request, queryset):
    """ЗДЕСЬ ВЫГРУЗКА"""
    print(2)


@admin.action(description="Удалить рассылку")
def delete(model_admin: admin.ModelAdmin, request, queryset):
    for notification in queryset:
        notification.state = NotificationState.deleted
        notification.save()


@admin.register(Notification, site=admin_site)
class NotificationAdmin(admin.ModelAdmin):
    # fields = ("text", "datetime")
    list_display = ("id", "text", "datetime", "state")
    list_filter = ("state",)

    # readonly_fields = ("id", "state")
    actions = (delete, export_competed)

    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST['action'] == 'export_competed':
            if not request.POST.getlist(ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                for u in Notification.objects.all():
                    post.update({ACTION_CHECKBOX_NAME: str(u.id)})
                request._set_post(post)
        return super(NotificationAdmin, self).changelist_view(request, extra_context)

    def get_action_choices(self, request, *args, **kwargs):
        choices = super(NotificationAdmin, self).get_action_choices(request)
        choices.pop(0)
        choices.reverse()
        return choices

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
