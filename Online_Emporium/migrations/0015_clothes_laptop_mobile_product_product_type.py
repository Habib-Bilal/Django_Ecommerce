# Generated by Django 4.2.4 on 2023-08-19 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Emporium', '0014_remove_mobilephone_product_ptr_delete_laptop_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Online_Emporium.product')),
                ('color', models.CharField(default=None, max_length=50)),
            ],
            bases=('Online_Emporium.product',),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Online_Emporium.product')),
                ('ram', models.IntegerField(default=None)),
                ('storage_type', models.CharField(default=None, max_length=100)),
                ('generation', models.CharField(default=None, max_length=50)),
            ],
            bases=('Online_Emporium.product',),
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Online_Emporium.product')),
                ('ram', models.IntegerField(default=None)),
            ],
            bases=('Online_Emporium.product',),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('laptop', 'Laptop'), ('mobile', 'Mobile'), ('clothes', 'Clothes')], default=None, max_length=10),
        ),
    ]
