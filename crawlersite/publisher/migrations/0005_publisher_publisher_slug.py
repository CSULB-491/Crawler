# Generated by Django 2.2.10 on 2020-03-08 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0004_author_author_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='publisher_slug',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
