from django.db import models

from admin_web.models import User


class Ticket(models.Model):
    class Meta:
        managed = False
        db_table = 'tickets'
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets_users", verbose_name="Пользователь")
    ticket_id = models.BigIntegerField(verbose_name="ID билета")
    state = models.CharField(max_length=16, verbose_name="Состояние")

    def __str__(self):
        return f"{self.id} - {self.ticket_id} ({self.state})"
