# Generated by Django 2.1.3 on 2018-11-13 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MOORA', '0004_auto_20181113_0245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bobot',
            name='kriteria',
        ),
        migrations.AddField(
            model_name='bobot',
            name='name_kriteria',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MOORA.NameKriteria'),
        ),
    ]