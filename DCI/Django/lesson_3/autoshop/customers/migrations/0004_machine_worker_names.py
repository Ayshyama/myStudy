# Generated by Django 4.2.6 on 2023-10-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0003_worker_machine"),
    ]

    operations = [
        migrations.AddField(
            model_name="machine",
            name="worker_names",
            field=models.TextField(
                blank=True, verbose_name=models.CharField(max_length=200)
            ),
        ),
    ]
