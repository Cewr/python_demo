# Generated by Django 3.2.6 on 2022-01-14 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_chess_ls'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chess',
            old_name='ls',
            new_name='list',
        ),
    ]
