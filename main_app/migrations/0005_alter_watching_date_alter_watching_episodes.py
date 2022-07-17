# Generated by Django 4.0.6 on 2022-07-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_watching'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watching',
            name='date',
            field=models.DateField(verbose_name='Watch Date'),
        ),
        migrations.AlterField(
            model_name='watching',
            name='episodes',
            field=models.PositiveSmallIntegerField(verbose_name='Episodes Watched'),
        ),
    ]
