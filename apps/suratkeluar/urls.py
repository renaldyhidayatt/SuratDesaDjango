from django.urls import path
from .views import suratKeluarList, suratKeluarCreate, suratKeluarUpdate, suratKeluarDelete

urlpatterns = [
    path("", suratKeluarList, name="suratkeluar"),
    path("create/", suratKeluarCreate, name="suratkeluarcreate"),
    path("update/<int:id>", suratKeluarUpdate, name="suratkeluarupdate"),
    path("delete/<int:id>", suratKeluarDelete, name="suratkeluardelete"),
]