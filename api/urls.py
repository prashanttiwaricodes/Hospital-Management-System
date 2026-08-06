from django.urls import path
from .views import PatientListAPIView,PatientDetailAPIView,DoctorListAPIView

urlpatterns=[
    path("patients/",PatientListAPIView.as_view(),name="patient-list"),
    path("patients/<int:pk>/",PatientDetailAPIView.as_view(),name="patient-detail"),
    path("doctors/",DoctorListAPIView.as_view(),name="doctor-list"),
]