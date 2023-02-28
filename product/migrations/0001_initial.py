# Generated by Django 4.1.7 on 2023-02-27 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20, unique=True, verbose_name='產品分類')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=255, verbose_name='產品詳細內容')),
                ('cat_image', models.ImageField(blank=True, null=True, upload_to='photos/categories')),
            ],
        ),
    ]