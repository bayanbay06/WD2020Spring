# Generated by Django 2.1.1 on 2020-03-14 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
