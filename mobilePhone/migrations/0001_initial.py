# Generated by Django 4.0.2 on 2022-03-25 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_alter_product_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='product.product')),
                ('code', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('ram', models.CharField(blank=True, max_length=200, null=True)),
                ('cpu', models.CharField(blank=True, max_length=200, null=True)),
                ('camera', models.CharField(blank=True, max_length=200, null=True)),
                ('audio', models.CharField(blank=True, max_length=200, null=True)),
                ('screen_size', models.CharField(blank=True, max_length=200, null=True)),
                ('display', models.CharField(blank=True, max_length=200, null=True)),
                ('Sim', models.CharField(blank=True, max_length=200, null=True)),
                ('GPS', models.CharField(blank=True, max_length=200, null=True)),
                ('enternal_ports', models.CharField(blank=True, max_length=200, null=True)),
                ('battery', models.CharField(blank=True, max_length=200, null=True)),
                ('wifi', models.CharField(blank=True, max_length=200, null=True)),
                ('color', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
