from django.db import models


class NotificationState:
    waiting = "waiting"
    completed = "completed"
    deleted = "deleted"


class Notification(models.Model):
    class Meta:
        managed = False
        db_table = 'notifications'
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

    id = models.AutoField(primary_key=True)

    text = models.CharField(max_length=4096, verbose_name="Текст", blank=True)
    datetime = models.DateTimeField(verbose_name="Время", null=True, blank=True)
    state = models.CharField(max_length=16, verbose_name="Состояние", null=True, default=NotificationState.waiting,
                             choices=((NotificationState.waiting, NotificationState.waiting),
                                      (NotificationState.completed, NotificationState.completed),
                                      (NotificationState.deleted, NotificationState.deleted)))

    def __str__(self):
        return f"Уведомление #{self.id}"
