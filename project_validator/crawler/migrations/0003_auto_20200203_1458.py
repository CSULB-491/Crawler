# Generated by Django 2.2.9 on 2020-02-03 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_auto_20200202_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='lastName',
            new_name='last_name',
        ),
    ]
