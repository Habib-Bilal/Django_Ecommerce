# Generated by Django 4.2.4 on 2023-09-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Emporium', '0037_remove_product_apparel_type_remove_product_battery_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details_image_1',
            field=models.ImageField(default=None, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='details_image_2',
            field=models.ImageField(default=None, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='details_image_3',
            field=models.ImageField(default=None, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='details_image_4',
            field=models.ImageField(default=None, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='details_image_5',
            field=models.ImageField(default=None, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
