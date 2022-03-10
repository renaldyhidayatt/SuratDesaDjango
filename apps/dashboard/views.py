from django.shortcuts import render
from apps.suratkeluar.models import SuratKeluar
from apps.suratmasuk.models import Suratmasuk
from apps.disposisi.models import Disposisi

# Create your views here.
def dashboard(request):
    suratmasuk = Suratmasuk.objects.all().count()
    suratkeluar = SuratKeluar.objects.all().count()
    disposisi = Disposisi.objects.all().count()

    context = {
        "suratmasuk": suratmasuk,
        "suratkeluar": suratkeluar,
        "disposisi": disposisi
    }

    return render(request, "index.html", context)