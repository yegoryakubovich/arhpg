from django.contrib import admin
from django.http import HttpResponseRedirect

from admin_web.admin import admin_site
from admin_web.filters import MultiSelectRelatedFieldListFilter
from admin_web.models import User, Notification, NotificationUser


@admin.action(description="Выбрать для рассылки")
def add_notification(model_admin: admin.ModelAdmin, request, queryset):
    notification = Notification.objects.create()
    for user in queryset:
        NotificationUser.objects.create(notification=notification, user=user)
    return HttpResponseRedirect(f'/admin/admin_web/notification/{notification.id}/change/')


@admin.register(User, site=admin_site)
class UserAdmin(admin.ModelAdmin):
    list_display = ("arhpg_id", "firstname", "lastname", "email")
    list_filter = (("tags", MultiSelectRelatedFieldListFilter),)
    actions = (add_notification,)

    def get_action_choices(self, request, *args, **kwargs):
        choices = super(UserAdmin, self).get_action_choices(request)
        choices.pop(0)
        choices.reverse()
        return choices

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
