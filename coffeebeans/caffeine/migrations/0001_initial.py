# Generated by Django 4.1.7 on 2024-01-27 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Coffee",
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
                ("name", models.CharField(max_length=100)),
                ("size", models.CharField(max_length=100)),
                ("cup_size", models.CharField(max_length=100)),
                ("espresso", models.CharField(max_length=100)),
                ("total_mgs", models.CharField(max_length=100)),
            ],
        ),
    ]
