# Generated by Django 2.2.5 on 2019-12-06 16:49

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
                ('description', models.CharField(blank=True, max_length=191, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('photo', models.ImageField(upload_to=products.models.path_and_rename)),
                ('description', models.CharField(blank=True, max_length=191, null=True)),
                ('stock', models.CharField(max_length=80)),
                ('price', models.CharField(max_length=191)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_products', to='products.Category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
