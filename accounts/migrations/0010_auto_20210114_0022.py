# Generated by Django 3.1.1 on 2021-01-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_tbluser_lasttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbluser',
            name='lastTime',
            field=models.CharField(default='01:00:00', max_length=20),
        ),
    ]
