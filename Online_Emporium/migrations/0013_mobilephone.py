# Generated by Django 4.2.4 on 2023-08-19 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Emporium', '0012_laptop'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Online_Emporium.product')),
                ('screen_size', models.CharField(max_length=10)),
                ('camera_resolution', models.CharField(max_length=20)),
                ('battery_capacity', models.CharField(max_length=10)),
            ],
            bases=('Online_Emporium.product',),
        ),
    ]