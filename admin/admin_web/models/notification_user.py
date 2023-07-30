from django.db import models

from admin_web.models import Notification, User


class NotificationUser(models.Model):
    class Meta:
        managed = False
        db_table = 'notifications_users'
        verbose_name = 'Уведомление - Пользователь'
        verbose_name_plural = 'Уведомление - Пользователи'

    id = models.AutoField(primary_key=True)

    notification = models.ForeignKey(Notification, on_delete=models.CASCADE,
                                     related_name="notifications_users_notifications", verbose_name="Уведомление")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="notifications_users_user", verbose_name="Пользователь")

    def __str__(self):
        return f"{self.id}"
