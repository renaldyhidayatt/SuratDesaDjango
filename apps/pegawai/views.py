from django.shortcuts import render, redirect
from .models import Pegawai
from apps.users.models import Users

# Create your views here.
def pegawaiAll(request):
    pegawai = Pegawai.objects.all()

    context = {
        "pegawai": pegawai
    }

    return render(request,"pegawai/index.html", context)


def pegawaiCreate(request):
    user = Users.objects.all()

    context = {
        "user": user
    }
    if request.method == "POST":
        nip = request.POST["nip"]
        nama = request.POST["nama"]
        pangkat = request.POST["pangkat"]
        jabatan = request.POST["jabatan"]
        user = request.POST["user"]

        users_id = Users.objects.get(email=user)

        Pegawai.objects.create(
            nip=nip,
            nama=nama,
            pangkat=pangkat,
            jabatan=jabatan,
            users=user
        )

        return redirect("pegawai")
    else:
        return render(request, "pegawai/create.html", context)



def pegawaiUpdate(request,id):
    user = Users.objects.all()
    pegawai_id = Pegawai.objects.get(id=id)
    context = {
        "pegawai": pegawai_id,
        "user": user
    }
    if request.method == "POST":
        nip = request.POST["nip"]
        nama = request.POST["nama"]
        pangkat = request.POST["pangkat"]
        jabatan = request.POST["jabatan"]
        user = request.POST["user"]

        users_id = Users.objects.get(email=user)

        pegawai_id.nip = nip
        pegawai_id.nama = nama
        pegawai_id.pangkat =pangkat
        pegawai_id.jabatan = jabatan
        pegawai_id.users = users_id

        pegawai_id.save()
        
    else:
        return render(request, "pegawait/update.html", context)



def pegawaiDelete(request, id):
    pegawai_id = Pegawai.objects.get(id=id)

    try:
        pegawai_id.delete()
        
        return redirect("pegawai")
    except Pegawai.DoesNotExist:
        raise Exception("Pegawai")