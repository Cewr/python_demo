# Generated by Django 3.2.6 on 2022-01-14 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chess',
            name='ls',
            field=models.CharField(default=(1, 2, 3), max_length=1000),
            preserve_default=False,
        ),
    ]
