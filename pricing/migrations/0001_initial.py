# Generated by Django 5.0.2 on 2024-02-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Price",
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
                    "base_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "prompt_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "completion_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                ("date", models.DateField()),
                ("model", models.CharField(max_length=100)),
                ("company", models.CharField(max_length=100)),
                ("endpoint", models.CharField(max_length=100)),
                (
                    "calculation_type",
                    models.CharField(
                        choices=[("tokens", "Tokens"), ("images", "Images")],
                        max_length=100,
                    ),
                ),
                ("size", models.CharField(max_length=100)),
                ("quality", models.CharField(max_length=100)),
            ],
        ),
    ]
