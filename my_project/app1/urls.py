from django.urls import path
from . import views

urlpatterns = [
    path("add_user/",views.add_user,name="add_user"),
    path("add_file/", views.add_file, name="add_file"),
    path("all_files/",views.all_files,name="all_files")
]
