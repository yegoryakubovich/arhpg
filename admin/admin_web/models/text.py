from django.db import models

from admin_web.models import CategoryText


class Text(models.Model):
    class Meta:
        managed = False
        db_table = 'texts'
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'

    id = models.AutoField(primary_key=True)

    category = models.ForeignKey(CategoryText, on_delete=models.CASCADE,
                                 related_name="texts_categories_texts", verbose_name="Категория")
    key = models.CharField(max_length=256, verbose_name="Ключ")
    value = models.CharField(max_length=8192, verbose_name="Значение")

    def __str__(self):
        return f"{self.key}"
