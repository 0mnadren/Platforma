# Generated by Django 3.2.6 on 2021-08-23 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_alter_programskipozivpitanje_odgovor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anketapitanje',
            name='anketa',
        ),
        migrations.RemoveField(
            model_name='programskipoziv',
            name='oblast',
        ),
        migrations.RemoveField(
            model_name='programskipozivpitanje',
            name='programski_poziv',
        ),
        migrations.RemoveField(
            model_name='prosledjenrad',
            name='profil',
        ),
        migrations.RemoveField(
            model_name='prosledjenrad',
            name='rad',
        ),
        migrations.RemoveField(
            model_name='rad',
            name='oblasti',
        ),
        migrations.RemoveField(
            model_name='rad',
            name='profil',
        ),
        migrations.DeleteModel(
            name='Anketa',
        ),
        migrations.DeleteModel(
            name='AnketaPitanje',
        ),
        migrations.DeleteModel(
            name='ProgramskiPoziv',
        ),
        migrations.DeleteModel(
            name='ProgramskiPozivPitanje',
        ),
        migrations.DeleteModel(
            name='ProsledjenRad',
        ),
        migrations.DeleteModel(
            name='Rad',
        ),
    ]
