# Generated by Django 4.1.1 on 2022-12-18 15:45

from django.db import migrations, models
import photo.models


class Migration(migrations.Migration):

    dependencies = [
        ("photo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Orders",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "customer",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="Заказчик"
                    ),
                ),
                (
                    "paper_type",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="Тип бумаги"
                    ),
                ),
                (
                    "format",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="Формат"
                    ),
                ),
                (
                    "document_type",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=100,
                        verbose_name="Тип документа",
                    ),
                ),
                (
                    "instance_count",
                    models.CharField(
                        db_index=True,
                        max_length=100,
                        verbose_name="Количество экземпляров",
                    ),
                ),
                (
                    "page_count",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="Количество страниц"
                    ),
                ),
                (
                    "price",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="Цена"
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to=photo.models.user_directory_path, verbose_name="Файл"
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
                "ordering": ["id"],
            },
        ),
    ]
