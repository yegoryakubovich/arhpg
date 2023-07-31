from django.db import models

from admin_web.models import Notification, User


class NotificationReportState:
    error = "error"
    completed = "completed"

    choices = ((error, error), (completed, completed))
    translate = {error: "Ошибка", completed: "Отправлено"}


class NotificationReport(models.Model):
    class Meta:
        managed = False
        db_table = 'notifications_reports'
        verbose_name = 'Уведомление - отчёт'
        verbose_name_plural = 'Уведомление - отчёты'

    id = models.AutoField(primary_key=True)

    notification = models.ForeignKey(Notification, on_delete=models.CASCADE,
                                     related_name="notifications_reports_notifications", verbose_name="Уведомление")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="notifications_reports_user", verbose_name="Пользователь")
    state = models.CharField(max_length=16, choices=NotificationReportState.choices)
    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.id} ({self.state})"
