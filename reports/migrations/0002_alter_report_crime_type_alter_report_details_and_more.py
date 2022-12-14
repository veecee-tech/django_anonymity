# Generated by Django 4.1.3 on 2022-11-15 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='crime_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='details',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='file',
            field=models.FileField(null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='report',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='regarding',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
