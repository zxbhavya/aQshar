# Generated by Django 4.2.11 on 2024-03-28 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0002_catalog_delete_item"),
    ]

    operations = [
        migrations.CreateModel(
            name="Catalogue",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("price", models.FloatField()),
                ("sell_or_donate", models.CharField(max_length=255)),
                ("negotiable_price", models.BooleanField(default=True)),
                ("seller_name", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="item_images"),
                ),
                ("is_sold", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="catalog.category",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Catalog",
        ),
    ]
