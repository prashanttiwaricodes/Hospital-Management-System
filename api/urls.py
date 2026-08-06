from django.urls import path
from .views import PatientListAPIView,DoctorListAPIView

urlpatterns=[
    path("patients/",PatientListAPIView.as_view(),name="patient-list"),
    path("doctors/",DoctorListAPIView.as_view(),name="doctor-list"),
]