# Generated by Django 4.2.11 on 2024-03-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_catalogue_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="catalogue",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]