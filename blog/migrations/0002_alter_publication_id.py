# Generated by Django 4.2.1 on 2023-05-26 20:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publication",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
