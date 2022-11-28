# Generated by Django 4.1.3 on 2022-11-13 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'superadmin'), (2, 'admin'), (3, 'reporter')], default=3),
        ),
    ]