# Generated by Django 3.2.6 on 2021-08-24 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programski_pozivi', '0003_alter_programskipoziv_naziv'),
        ('radovi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rad',
            name='programski_poziv',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='programski_pozivi.programskipoziv'),
        ),
    ]