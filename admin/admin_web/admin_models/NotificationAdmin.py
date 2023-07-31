import csv
from datetime import datetime, timedelta

from django.contrib import admin
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.http import HttpResponseRedirect
from openpyxl.workbook import Workbook
from openpyxl.worksheet.copier import WorksheetCopy
from openpyxl.worksheet.worksheet import Worksheet

from admin_web.admin import admin_site
from admin_web.models import Notification, NotificationReport, User
from admin_web.models.notification import NotificationState
from admin_web.models.notification_report import NotificationReportState


@admin.action(description="Выгрузить логи отправленных уведомлений")
def export_competed(model_admin: admin.ModelAdmin, request, queryset):
    all_data = [["ID", "Текст сообщения", "Leader ID", "Статус отправки", "Время"]]
    for notify_report in NotificationReport.objects.all():
        notify: Notification = Notification.objects.filter(id=notify_report.notification_id).first()
        if not notify:
            print(f"NOTIFY_REPORT #{notify_report.id}: Notification not found")

        user: User = User.objects.filter(id=notify_report.user_id).first()
        if not user:
            print(f"NOTIFY_REPORT #{notify_report.id}: User not found")

        all_data.append([
            notify_report.id, notify.text, user.arhpg_id, NotificationReportState.translate[notify_report.state],
            (notify.datetime + timedelta(hours=3)).strftime("%d.%m.%y %H:%M")
        ])

        wb = Workbook()
        wb.remove(wb.active)
        ws: Worksheet = wb.create_sheet("Выгрузка")
        for data in all_data:
            ws.append(data)
        for column in ["A", "B", "C", "D", "E"]:
            if column in ["A"]:
                ws.column_dimensions[column].width = 5
            elif column in ["B"]:
                ws.column_dimensions[column].width = 40
            else:
                ws.column_dimensions[column].width = 20
        filename = f"media/exports/notification_{datetime.now().strftime('%y_%m_%d_%H_%M')}"
        wb.save(f"{filename}.xlsx")
        return HttpResponseRedirect(f"/{filename}.xlsx")


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
