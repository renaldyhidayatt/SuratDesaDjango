from django.db import models
from apps.utils.models import Timestamp
from datetime import datetime
from apps.pegawai.models import Pegawai
from django.utils.timezone import now

# Create your models here.
class SuratKeluar(Timestamp):
    no_surat = models.CharField(max_length=50)
    kode_surat = models.CharField(max_length=50)
    tgl_keluar = models.DateField(default=now)
    ditujukan = models.CharField(max_length=100)
    perihal = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=200)
    kategori = models.CharField(max_length=15)
    image = models.ImageField()
    status = models.CharField(max_length=10)
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
    lampiran = models.CharField(max_length=100)
    sifat = models.CharField(max_length=100)


    def __str__(self):
        return self.no_surat
