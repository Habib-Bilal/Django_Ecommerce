# Generated by Django 4.2.4 on 2023-10-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Emporium', '0061_order_ordered_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered_quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_quantity',
            field=models.ManyToManyField(blank=True, related_name='orders', to='Online_Emporium.cartitem'),
        ),
    ]
