# Generated by Django 3.2.6 on 2021-08-27 18:55

from django.db import migrations, models
import profil.validators


class Migration(migrations.Migration):

    dependencies = [
        ('radovi', '0003_auto_20210824_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prosledjenrad',
            name='konacna_odluka',
        ),
        migrations.AddField(
            model_name='prosledjenrad',
            name='zakljucani_odgovori',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rad',
            name='prihvacen_rad',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='rad',
            name='biografije',
            field=models.FileField(upload_to='radovi/biografije/pdfs', validators=[profil.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='rad',
            name='datum_podnosenja',
            field=models.DateField(help_text='Use the following format: YYYY-MM-DD'),
        ),
        migrations.AlterField(
            model_name='rad',
            name='kategorija',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='rad',
            name='naziv',
            field=models.CharField(max_length=225, unique=True),
        ),
        migrations.AlterField(
            model_name='rad',
            name='opis',
            field=models.FileField(upload_to='radovi/opis/pdfs', validators=[profil.validators.validate_file_extension]),
        ),
    ]
