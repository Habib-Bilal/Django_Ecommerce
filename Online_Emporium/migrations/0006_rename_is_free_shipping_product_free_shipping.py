# Generated by Django 4.2.4 on 2023-08-12 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Emporium', '0005_remove_product_details_page_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_free_shipping',
            new_name='free_shipping',
        ),
    ]
