from django.db import models
from django.urls import reverse

class Documents(models.Model):
    type = models.CharField(max_length=100, db_index=True, verbose_name="Тип бумаги")
    format = models.CharField(max_length=100, db_index=True, verbose_name="Формат")
    document = models.CharField(max_length=100,blank=True, db_index=True, verbose_name="Документ")
    price = models.CharField(max_length=100, db_index=True, verbose_name="Цена")

    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'
        ordering = ['id']

