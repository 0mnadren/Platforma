# Generated by Django 3.2.6 on 2021-09-09 18:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radovi', '0004_auto_20210827_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rad',
            name='datum_podnosenja',
            field=models.DateField(help_text='Koristi sledeći format: GGGG-MM-DD'),
        ),
        migrations.AlterField(
            model_name='rad',
            name='godina',
            field=models.PositiveIntegerField(help_text='Koristi sledeći format: GGGG', validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)]),
        ),
    ]
