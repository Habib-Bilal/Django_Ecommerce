# Generated by Django 4.2.4 on 2023-09-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Emporium', '0042_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='provence',
            field=models.CharField(blank=True, default=None, max_length=30),
        ),
    ]