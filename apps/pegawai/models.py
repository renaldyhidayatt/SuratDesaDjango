from django.db import models
from apps.utils.models import Timestamp
from apps.users.models import Users

# Create your models here.
class Pegawai(Timestamp):
    nip = models.CharField(max_length=30)
    nama = models.CharField(max_length=100)
    pangkat = models.CharField(max_length=30)
    jabatan = models.CharField(max_length=30)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama