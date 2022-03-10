from django.urls import path
from .views import suratMasukList, suratMasukCreate, suratMasukUpdate, suratMasukDelete

urlpatterns = [
    path("", suratMasukList, name="suratmasuk"),
    path("create/", suratMasukCreate, name="suratmasukcreate"),
    path("update/<int:id>", suratMasukUpdate, name="suratmasukupdate"),
    path("delete/<int:id>", suratMasukDelete, name="suratmasukdelete"),

]