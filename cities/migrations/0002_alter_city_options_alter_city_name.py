# Generated by Django 4.1.5 on 2023-01-19 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cities", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="city",
            options={
                "ordering": ["name"],
                "verbose_name": "Місто",
                "verbose_name_plural": "Містa",
            },
        ),
        migrations.AlterField(
            model_name="city",
            name="name",
            field=models.CharField(max_length=150, unique=True, verbose_name="Місто"),
        ),
    ]
