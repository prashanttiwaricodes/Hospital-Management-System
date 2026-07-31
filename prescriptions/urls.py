from django.urls import path
from . import views

urlpatterns=[
    path("",views.prescription_list,name="prescription_list"),
    path("add/",views.prescription_add,name="prescription_add"),
    path("edit/<int:pk>/",views.prescription_edit,name="prescription_edit"),
    path("delete/<int:pk>/",views.prescription_delete,name="prescription_delete"),
]