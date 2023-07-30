from django.db import models


class Setting(models.Model):
    class Meta:
        managed = False
        db_table = 'settings'
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

    id = models.AutoField(primary_key=True)

    key = models.CharField(max_length=256, verbose_name="Ключ")
    value = models.CharField(max_length=256, verbose_name="Значение")

    def __str__(self):
        return f"{self.key} "
