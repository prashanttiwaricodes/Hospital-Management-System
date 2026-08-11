from rest_framework.views import APIView
from rest_framework.response import Response
from patients.models import Patient
from patients.serializers import PatientSerializer
from rest_framework import status
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
from departments.models import Department
from departments.serializers import DepartmentSerializer
from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer
from prescriptions.models import Prescription
from prescriptions.serializers import PrescriptionSerializer
from billing.models import Bill
from billing.serializers import BillSerializer

# Create your views here.

# ------API View--------------   

class PatientListAPIView(APIView):

   def get(self,request):
      patients=Patient.objects.all()

      serializer=PatientSerializer(patients,many=True)

      return Response(serializer.data)



   def post(self,request):
      serializer=PatientSerializer(data=request.data) 
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)  
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class PatientDetailAPIView(APIView):
   def get_object(self,pk):
      return Patient.objects.get(pk=pk)

   def get(self,request,pk):
      patient=self.get_object(pk)
      serializer=PatientSerializer(patient)   
      return Response(serializer.data)

   def put(self,request,pk):
      patient=self.get_object(pk)

      serializer=PatientSerializer(patient,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)

      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


   def delete(self,request,pk):
      patient=self.get_object(pk)
      patient.delete()

      return Response(
         {"message":"Patient Deleted Successfully"},
         status=status.HTTP_204_NO_CONTENT
      )





# ------API View--------------   

class DoctorListAPIView(APIView):

   def get(self,request):
      doctors=Doctor.objects.all()

      serializer=DoctorSerializer(doctors,many=True)

      return Response(serializer.data)



   def post(self,request):
      serializer=DoctorSerializer(data=request.data) 
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)  
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





  #-------ModelViewSet-----------
from rest_framework.viewsets import ModelViewSet  
from rest_framework.permissions import IsAuthenticated 
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

class PatientViewSet(ModelViewSet):
   queryset=Patient.objects.all()
   serializer_class=PatientSerializer

   permission_classes=[IsAdminOrReadOnly]
   filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
   filterset_fields=["gender","blood_group"]
   search_fields=["name","address"]
   ordering_fields=["name","age","id"]
   ordering=["id"]





class DoctorViewSet(ModelViewSet):  
   queryset=Doctor.objects.all()
   serializer_class=DoctorSerializer

   permission_classes=[IsAdminOrReadOnly] 
   filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
   filterset_fields=["specialization"]
   search_fields=["name","specialization"]
   ordering_fields=["name","id"]
   ordering=["id"]




class DepartmentViewSet(ModelViewSet):
   queryset=Department.objects.all() 
   serializer_class=DepartmentSerializer

   permission_classes=[IsAdminOrReadOnly]
   filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
   search_fields=["name"]
   ordering_fields=["id"]




class AppointmentViewSet(ModelViewSet):
   queryset=Appointment.objects.all()
   serializer_class=AppointmentSerializer   

   permission_classes=[IsAdminOrReadOnly]
   filter_backends=[DjangoFilterBackend,OrderingFilter]
   filterset_fields=["status"]
   ordering_fields=["id","appointment_date"]
   ordering=["appointment_date"]



class PrescriptionViewSet(ModelViewSet):
   queryset=Prescription.objects.all()
   serializer_class=PrescriptionSerializer

   permission_classes=[IsAdminOrReadOnly]








class BillViewSet(ModelViewSet):
   queryset=Bill.objects.all() 
   serializer_class=BillSerializer

   permission_classes=[IsAdminOrReadOnly]
   filter_backends=[DjangoFilterBackend,SearchFilter]
   search_fields=["patient__name"]

      

   


   
