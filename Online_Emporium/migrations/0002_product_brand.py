# Generated by Django 4.2.4 on 2023-08-12 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Emporium', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
