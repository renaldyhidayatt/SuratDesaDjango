from django.db import models
from apps.utils.models import Timestamp
# from datetime import datetime
from django.utils.timezone import now
from apps.pegawai.models import Pegawai
from apps.suratmasuk.models import Suratmasuk

# Create your models here.
class Disposisi(Timestamp):
    no_surat = models.CharField(max_length=10)
    diteruskan = models.CharField(max_length=100)
    dari = models.CharField(max_length=100)
    dgn_hormat = models.CharField(max_length=100)
    tgl_surat = models.DateField(default=now)
    tgl_diterima = models.DateField(default=now)
    sifat = models.CharField(max_length=100)
    perihal = models.TextField()
    catatan = models.TextField()
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
    smasuk = models.ForeignKey(Suratmasuk, on_delete=models.CASCADE)
    v_read = models.IntegerField()
    tanggapan = models.TextField()
    tujuan = models.TextField()
    teruntuk = models.CharField(max_length=150)


    def __str__(self):
        return self.no_surat
