# Generated by Django 5.1.5 on 2025-01-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_personage_gamer_alter_gamer_personages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamer',
            name='personages',
            field=models.ManyToManyField(blank=True, related_name='gamers', to='mysite.personage', verbose_name='Персонажи'),
        ),
    ]
