from django.shortcuts import render, redirect
from .models import Suratmasuk
from apps.pegawai.models import Pegawai

# Create your views here.
def suratMasukList(request):
    suratmasuk = Suratmasuk.objects.all()

    context = {
        "suratmasuk": suratmasuk
    }

    return render(request, "suratmasuk/index.html", context)


def suratMasukCreate(request):
    pegawai_all = Pegawai.objects.all()
    context = {
        "pegawai": pegawai_all
    }
    if request.method == "POST":
        no_surat = request.POST["no_surat"]
        kode_surat = request.POST["kode_surat"]
        kategori = request.POST["kategori"]
        pengirim = request.POST["pengirim"]
        perihal = request.POST["perihal"]
        tgl_masuk = request.POST["tgl_masuk"]
        ditujukan = request.POST["ditujukan"]
        keterangan = request.POST["keterangan"]
        image = request.FILES["image"]
        pegawai = request.POST["pegawai"]

        pegawai_id = Pegawai.objects.get(nama=pegawai)

        Suratmasuk.objects.create(
            no_surat=no_surat,
            kode_surat=kode_surat,
            kategori=kategori,
            pengirim=pengirim,
            perihal=perihal,
            tgl_masuk=tgl_masuk,
            ditujukan=ditujukan,
            keterangan=keterangan,
            image=image,
            pegawai=pegawai_id
        )

        return redirect("suratmasuk")

    else:
        return render(request, "suratmasuk/create.html", context)


def suratMasukUpdate(request, id):
    pegawai = Pegawai.objects.all()
    suratmasuk_id = Suratmasuk.objects.get(id=id)

    context = {
        "pegawai": pegawai,
        "suratmasuk": suratmasuk_id
    }

    if request.method == "POST":
        no_surat = request.POST["no_surat"]
        kode_surat = request.POST["kode_surat"]
        kategori = request.POST["kategori"]
        pengirim = request.POST["pengirim"]
        perihal = request.POST["perihal"]
        tgl_masuk = request.POST["tgl_masuk"]
        ditujukan = request.POST["ditujukan"]
        keterangan = request.POST["keterangan"]
        image = request.FILES["image"]
        pegawai = request.POST["pegawai"]

        pegawai_id = Pegawai.objects.get(nama=pegawai)
    
        suratmasuk_id.no_surat = no_surat
        suratmasuk_id.kode_surat = kode_surat
        suratmasuk_id.kategori = kategori
        suratmasuk_id.pengirim = pengirim
        suratmasuk_id.perihal = perihal
        suratmasuk_id.tgl_masuk = tgl_masuk
        suratmasuk_id.ditujukan = ditujukan
        suratmasuk_id.keterangan = keterangan
        suratmasuk_id.image = image
        suratmasuk_id.pegawai = pegawai

        suratmasuk_id.save()

        return redirect("suratmasuk")
    else:
        return render(request, "suratmasuk/update.html", context)



def suratMasukDelete(request, id):
    suratmasuk = Suratmasuk.objects.get(id=id)

    try:
        suratmasuk.delete()

        return redirect("suratmasuk")
    except Suratmasuk.DoesNotExist:
        raise Exception("Doesnt npt")