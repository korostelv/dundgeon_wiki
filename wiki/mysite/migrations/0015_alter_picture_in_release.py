# Generated by Django 5.1.6 on 2025-02-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_picture_in_release'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='in_release',
            field=models.BooleanField(default=False, verbose_name='Показывать в выпусках'),
        ),
    ]
