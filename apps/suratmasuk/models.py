from django.db import models
from apps.utils.models import Timestamp
from apps.pegawai.models import Pegawai
from django.utils.timezone import now

# Create your models here.
class Suratmasuk(Timestamp):
    no_surat = models.CharField(max_length=30)
    kode_surat = models.CharField(max_length=30)
    kategori = models.CharField(max_length=29)
    pengirim = models.CharField(max_length=50, null=False)
    perihal = models.TextField()
    tgl_masuk = models.DateField(default=now)
    ditujukan = models.CharField(max_length=50)
    keterangan = models.TextField(null=False)
    image = models.ImageField()
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE)

    def __str__(self):
        return self.no_surat