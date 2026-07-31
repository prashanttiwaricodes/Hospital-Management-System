from django.urls import path
from . import views

urlpatterns=[
    path("",views.bills_list,name="bills_list"),
    path("add/",views.bills_add,name="bills_add"),
    path("edit/<int:pk>/",views.bills_edit,name="bills_edit"),
    path("delete/<int:pk>/",views.bills_delete,name="bills_delete"),
]