# Generated by Django 2.2.10 on 2020-03-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0005_publisher_publisher_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='publisher_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
