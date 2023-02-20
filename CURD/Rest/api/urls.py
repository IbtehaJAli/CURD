from django.urls import path
from .views import(Listview,update,destroy,create,displayData)
urlpatterns=[
    path("",Listview.as_view(),name="list"),
path("<pk>/update",update.as_view(),name="edit"),
path("<pk>/delete",destroy.as_view(),name="delete"),
path("create/",create.as_view(),name="new"),
path("<pk>/display",displayData.as_view(),name="display")
]