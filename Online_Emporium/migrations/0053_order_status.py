# Generated by Django 4.2.4 on 2023-10-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Emporium', '0052_alter_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_process', 'In Process'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='pending', max_length=20),
        ),
    ]