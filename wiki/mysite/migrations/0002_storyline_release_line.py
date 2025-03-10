# Generated by Django 5.1.5 on 2025-01-28 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storyline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=50, verbose_name='Сюжетная линия')),
            ],
        ),
        migrations.AddField(
            model_name='release',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.storyline', verbose_name='Сюжетная линия'),
        ),
    ]
