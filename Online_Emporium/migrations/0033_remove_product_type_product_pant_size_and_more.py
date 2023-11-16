# Generated by Django 4.2.4 on 2023-08-25 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Emporium', '0032_product_apparel_type_product_battery_product_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.AddField(
            model_name='product',
            name='pant_size',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pant_type',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='shoes_size',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
