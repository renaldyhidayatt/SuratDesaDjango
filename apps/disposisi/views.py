from django.shortcuts import render, redirect
from .models import Disposisi
from apps.suratmasuk.models import Suratmasuk
from apps.pegawai.models import Pegawai

# Create your views here.
def disposisiList(request):
    disposisi = Disposisi.objects.all()

    context = {
        "disposisi": disposisi
    }

    return render(request, "disposisi/index.html", context)

def disposisiCreate(request):
    pegawai_all = Pegawai.objects.all()
    suratmasuk_all = Suratmasuk.objects.all()

    context = {
        "pegawai_all": pegawai_all,
        "suratmasuk_all": suratmasuk_all
    }

    if request.method == 'POST':
        no_surat = request.POST["no_surat"]
        diteruskan = request.POST["diteruskan"]
        dari = request.POST["dari"]
        dgn_hormat = request.POST["dgn_hormat"]
        tgl_surat = request.POST["tgl_surat"]
        tgl_diterima = request.POST["tgl_diterima"]
        sifat = request.POST["sifat"]
        perihal = request.POST["perihal"]
        catatan = request.POST["catatan"]
        pegawai = request.POST["pegawai"]
        smasuk = request.POST["smasuk"]
        v_read = request.POST["v_read"]
        tanggapan = request.POST["tanggapan"]
        tujuan = request.POST["tujuan"]
        teruntuk = request.POST["teruntuk"]

        pegawai_id = Pegawai.objects.get(nama=pegawai)
        smasuk_id = Suratmasuk.objects.get(kode_surat=smasuk)

        Disposisi.objects.create(
            no_surat=no_surat,
            diteruskan=diteruskan,
            dari=dari,
            dgn_hormat=dgn_hormat,
            tgl_surat=tgl_surat,
            sifat=sifat,
            perihal=perihal,
            catatan=catatan,
            pegawai=pegawai_id,
            smasuk=smasuk_id,
            v_read=v_read,
            tanggapan=tanggapan,
            tujuan=tujuan,
            teruntuk=teruntuk
        )

        return redirect("disposisi")

    else:
        return render(request, "disposisi/create.html", context)



def disposisiUpdate(request, id):
    disposisi = Disposisi.objects.get(id=id)
    pegawai_all = Users.objects.all()
    suratmasuk_all = Suratmasuk.objects.all()

    context = {
        "disposisi": disposisi,
        "pegawai": pegawai_all,
        "suratmasuk": suratmasuk_all
    }

    if request.method == 'POST':
        no_surat = request.POST["no_surat"]
        diteruskan = request.POST["diteruskan"]
        dari = request.POST["dari"]
        dgn_hormat = request.POST["dgn_hormat"]
        tgl_surat = request.POST["tgl_surat"]
        tgl_diterima = request.POST["tgl_diterima"]
        sifat = request.POST["sifat"]
        perihal = request.POST["perihal"]
        catatan = request.POST["catatan"]
        pegawai = request.POST["pegawai"]
        smasuk = request.POST["smasuk"]
        v_read = request.POST["v_read"]
        tanggapan = request.POST["tanggapan"]
        tujuan = request.POST["tujuan"]
        teruntuk = request.POST["teruntuk"]

        disposisi.no_surat = no_surat
        disposisi.diteruskan = diteruskan
        disposisi.dari = dari
        disposisi.dgn_hormat = dgn_hormat
        disposisi.tgl_surat = tgl_surat
        disposisi.tgl_diterima = tgl_diterima
        disposisi.sifat = sifat
        disposisi.perihal = perihal
        disposisi.catatan = catatan

        pegawai_id = Pegawai.objects.get(nama=pegawai)
        suratmasuk_id = Suratmasuk.objects.get(kode_surat=smasuk)



        disposisi.pegawai = pegawai_id
        disposisi.smasuk = suratmasuk_id
        disposisi.v_read = v_read
        disposisi.tanggapan = tanggapan
        disposisi.tujuan = tujuan
        disposisi.teruntuk = teruntuk

        disposisi.save()

        return redirect("disposisi")
    else:
        return render(request, "disposisi/update.html", context)


def disposisiDelete(request, id):
    disposisi = Disposisi.objects.get(id=id)
    try:
        disposisi.delete()
    except Disposisi.DoesNotExist:
        raise Exception("Dispoisi")