# Generated by Django 4.2.4 on 2023-08-19 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Emporium', '0010_alter_product_star_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='d_image_1',
            field=models.ImageField(default=None, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='d_image_2',
            field=models.ImageField(default=None, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='d_image_3',
            field=models.ImageField(default=None, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='d_image_4',
            field=models.ImageField(default=None, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='d_image_5',
            field=models.ImageField(default=None, upload_to='products/'),
        ),
    ]
