from django.urls import path  #we need path to create urls.
from . import views   # . means current app(doctors).  so we are importing views.py

urlpatterns=[
    path("",views.doctor_list,name="doctor_list"),  #this means /doctors/    will call doctor_list()
    path("add/", views.doctor_add,name="doctor_add"),
    path("edit/<int:pk>/",views.doctor_edit,name="doctor_edit"),
     path("delete/<int:pk>/",views.doctor_delete,name="doctor_delete"),
]