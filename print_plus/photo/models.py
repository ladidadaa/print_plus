from django.db import models
from django.urls import reverse

class Documents(models.Model):
    type = models.CharField(max_length=100, db_index=True, verbose_name="Тип бумаги")
    format = models.CharField(max_length=100, db_index=True, verbose_name="Формат")
    document = models.CharField(max_length=100, blank=True, db_index=True, verbose_name="Документ")
    price = models.CharField(max_length=100, db_index=True, verbose_name="Цена")

    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'
        ordering = ['id']


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.customer, filename)


class Orders(models.Model):
    customer = models.CharField(max_length=100, db_index=True, verbose_name="Заказчик")
    paper_type = models.CharField(max_length=100, db_index=True, verbose_name="Тип бумаги")
    format = models.CharField(max_length=100, db_index=True, verbose_name="Формат")
    document_type = models.CharField(max_length=100, blank=True, db_index=True, verbose_name="Тип документа")
    instance_count = models.CharField(max_length=100, db_index=True, verbose_name="Количество экземпляров")
    page_count = models.CharField(max_length=100, db_index=True, verbose_name="Количество страниц")
    price = models.CharField(max_length=100, db_index=True, verbose_name="Цена")
    file = models.FileField(upload_to=user_directory_path, verbose_name="Файл")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['id']
