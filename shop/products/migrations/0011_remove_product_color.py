# Generated by Django 4.1.7 on 2023-04-06 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
    ]