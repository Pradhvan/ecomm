# Generated by Django 4.2 on 2023-04-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_productline"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(default="b-b-b-b", max_length=255),
            preserve_default=False,
        ),
    ]
