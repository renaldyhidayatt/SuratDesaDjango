from django.urls import path
from .views import pegawaiAll, pegawaiCreate, pegawaiUpdate, pegawaiDelete

urlpatterns = [
    path("", pegawaiAll, name="pegawai"),
    path("create/", pegawaiCreate, name="pegawaicreate"),
    path("update/<int:id>", pegawaiUpdate, name="pegawaiupdate"),
    path("delete/<int:id>", pegawaiDelete, name="pegawaidelete"),
]