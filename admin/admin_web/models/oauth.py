from django.db import models


class Oauth(models.Model):
    class Meta:
        managed = False
        db_table = 'oauths'
        verbose_name = 'Авторизация'
        verbose_name_plural = 'Авторизации'

    id = models.AutoField(primary_key=True)

    tg_user_id = models.BigIntegerField(verbose_name="TG ID")
    hash = models.CharField(max_length=1024, verbose_name="Хеш")
    token = models.CharField(max_length=1024, verbose_name="Токен")
    expired = models.DateTimeField(verbose_name="Истекает")

    def __str__(self):
        return f"{self.id}"
