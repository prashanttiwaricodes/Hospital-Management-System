from rest_framework.views import APIView
from rest_framework.response import Response
from patients.models import Patient
from patients.serializers import PatientSerializer
from rest_framework import status
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer

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
