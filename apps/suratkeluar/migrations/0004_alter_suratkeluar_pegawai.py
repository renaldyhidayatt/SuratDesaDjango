# Generated by Django 4.0.3 on 2022-03-10 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pegawai', '0001_initial'),
        ('suratkeluar', '0003_alter_suratkeluar_tgl_keluar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suratkeluar',
            name='pegawai',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pegawai.pegawai'),
        ),
    ]