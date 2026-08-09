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

class PatientViewSet(ModelViewSet):
   queryset=Patient.objects.all()
   serializer_class=PatientSerializer

   permission_classes=[IsAdminOrReadOnly]

   
