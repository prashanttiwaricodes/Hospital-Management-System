from django.urls import path,include
from .views import PatientListAPIView,PatientDetailAPIView,DoctorListAPIView,PatientViewSet,DoctorViewSet
from rest_framework.routers import DefaultRouter



router=DefaultRouter()
router.register("patients-v2",PatientViewSet)
router.register("doctors-v2",DoctorViewSet)

urlpatterns=[
    path("patients/",PatientListAPIView.as_view(),name="patient-list"),
    path("patients/<int:pk>/",PatientDetailAPIView.as_view(),name="patient-detail"),
    path("doctors/",DoctorListAPIView.as_view(),name="doctor-list"),
    path("",include(router.urls)),
]


