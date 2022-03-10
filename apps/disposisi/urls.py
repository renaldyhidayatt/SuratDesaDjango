from django.urls import path
from .views import disposisiList, disposisiCreate, disposisiUpdate, disposisiDelete


urlpatterns = [
    path("", disposisiList, name="disposisi"),
    path("create/", disposisiCreate, name="disposisicreate"),
    path("update/<int:id>", disposisiUpdate, name="disposisiupdate"),
    path("delete/<int:id>", disposisiDelete, name="disposisidelete")
]