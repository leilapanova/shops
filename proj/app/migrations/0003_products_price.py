# Generated by Django 5.0 on 2023-12-16 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_products_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
