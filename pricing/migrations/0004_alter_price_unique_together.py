# Generated by Django 5.0.2 on 2024-02-12 11:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pricing", "0003_alter_price_quality_alter_price_size"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="price",
            unique_together={("model", "company")},
        ),
    ]
