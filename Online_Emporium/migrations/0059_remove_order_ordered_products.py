# Generated by Django 4.2.4 on 2023-10-27 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Emporium', '0058_order_ordered_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered_products',
        ),
    ]
