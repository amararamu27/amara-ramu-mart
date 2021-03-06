# Generated by Django 2.2.13 on 2020-08-08 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=100)),
                ('contact', models.IntegerField(unique=True)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='customer_images/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=100, unique=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('photo', models.ImageField(upload_to='product_images/')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app18.CustomerModel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app18.ProductModel')),
            ],
        ),
    ]
