from django.shortcuts import render
from apps.suratkeluar.models import SuratKeluar
from apps.suratmasuk.models import Suratmasuk
from apps.disposisi.models import Disposisi
from apps.pegawai.models import Pegawai
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/auth/login')
def dashboard(request):
    suratmasuk = Suratmasuk.objects.all().count()
    suratkeluar = SuratKeluar.objects.all().count()
    disposisi = Disposisi.objects.all().count()
    pegawai  = Pegawai.objects.all().count()


    context = {
        "suratmasuk": suratmasuk,
        "suratkeluar": suratkeluar,
        "disposisi": disposisi,
        "pegawai": pegawai,
    }

    return render(request, "index.html", context)