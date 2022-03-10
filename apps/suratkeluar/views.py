from django.shortcuts import render, redirect
from .models import SuratKeluar
from apps.pegawai.models import Pegawai

# Create your views here.
def suratKeluarList(request):
    suratkeluar = SuratKeluar.objects.all()

    context = {
        "suratkeluar": suratkeluar
    }

    return render(request, "suratkeluar/index.html", context)


def suratKeluarCreate(request):
    pegawai_all = Pegawai.objects.all()
    context = {
        "pegawai": pegawai_all
    }
    if request.method == "POST":
        no_surat = request.POST["no_surat"]
        kode_surat = request.POST["kode_surat"]
        tgl_keluar = request.POST["tgl_keluar"]
        ditujukan = request.POST["ditujukan"]
        perihal = request.POST["perihal"]
        keterangan = request.POST["keterangan"]
        kategori = request.POST["kategori"]
        image = request.FILES["image"]
        status = request.POST["status"]
        pegawai = request.POST["pegawai"]
        lampiran = request.POST["lampiran"]
        sifat = request.POST["sifat"]

        pegawai_id = Pegawai.objects.get(nama=pegawai)

        SuratKeluar.objects.create(
            no_surat=no_surat,
            kode_surat=kode_surat,
            tgl_keluar=tgl_keluar,
            ditujukan=ditujukan,
            perihal=perihal,
            keterangan=keterangan,
            kategori=kategori,
            image=image,
            status=status,
            pegawai=pegawai_id,
            lampiran=lampiran,
            sifat=sifat
        )

        return redirect("pegawai")
    else:
        return render(request, "suratkeluar/create.html", context)



def suratKeluarUpdate(request, id):
    pegawai_all = Pegawai.objects.all()
    suratkeluar = SuratKeluar.objects.get(id=id)

    context = {
        "suratkeluar": suratkeluar,
        "pegawai": pegawai_all
    }

    if request.method == "POST":
        no_surat = request.POST["no_surat"]
        kode_surat = request.POST["kode_surat"]
        tgl_keluar = request.POST["tgl_keluar"]
        ditujukan = request.POST["ditujukan"]
        perihal = request.POST["perihal"]
        keterangan = request.POST["keterangan"]
        kategori = request.POST["kategori"]
        image = request.FILES["image"]
        status = request.POST["status"]
        pegawai = request.POST["pegawai"]
        lampiran = request.POST["lampiran"]
        sifat = request.POST["sifat"]

        pegawai_id = Pegawai.objects.get(nama=pegawai)


        suratkeluar.no_surat = no_surat
        suratkeluar.kode_surat = kode_surat
        suratkeluar.tgl_keluar = tgl_keluar
        suratkeluar.ditujukan = ditujukan
        suratkeluar.perihal = perihal
        suratkeluar.keterangan = keterangan
        suratkeluar.kategori = kategori
        suratkeluar.image = image
        suratkeluar.status = status
        suratkeluar.pegawai = pegawai_id
        suratkeluar.lampiran = lampiran
        suratkeluar.sifat = sifat

        suratkeluar.save()
    else:
        return render(request, "suratkeluar/update.html", context)




def suratKeluarDelete(request,id):
    suratkeluar = SuratKeluar.objects.get(id=id)
    try:
        suratkeluar.delete()
        return redirect("suratkeluar")
    except SuratKeluar.DoesNotExist:
        raise Exception("SuratKeluar")
