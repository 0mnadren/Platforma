# Generated by Django 3.2.6 on 2021-08-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='otvoren',
            field=models.BooleanField(default=False),
        ),
    ]
