# Generated by Django 4.0.3 on 2022-03-09 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suratkeluar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suratkeluar',
            name='tgl_keluar',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]