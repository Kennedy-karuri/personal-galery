# Generated by Django 3.1.5 on 2021-01-11 19:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='articles'),
        ),
    ]
