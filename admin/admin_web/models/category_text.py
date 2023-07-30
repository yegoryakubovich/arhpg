from django.db import models


class CategoryText(models.Model):
    class Meta:
        managed = False
        db_table = 'categories_texts'
        verbose_name = 'Текст - Категория'
        verbose_name_plural = 'Текст - Категории'

    id = models.IntegerField(primary_key=True, auto_created=True)

    name = models.CharField(max_length=16, verbose_name="Название")

    def __str__(self):
        return f"{self.name}"
