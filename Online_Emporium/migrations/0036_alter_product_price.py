# Generated by Django 4.2.4 on 2023-08-31 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Emporium', '0035_rename_star_ratings_product_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=None),
        ),
    ]
