# Generated by Django 4.2.4 on 2023-10-16 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Emporium', '0046_rename_is_admin_customuser_is_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_customer',
        ),
    ]
