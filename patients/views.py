from django.shortcuts import render,redirect,get_object_or_404
from .models import Patient
from .forms import PatientForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PatientSerializer
from rest_framework import status



# Create your views here.

@login_required
def patient_list(request):
    search=request.GET.get("search")
   
    patients=Patient.objects.all().order_by("id")

    if search:
       patients=patients.filter(name__icontains=search)

       
    paginator=Paginator(patients,5)

    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

   

    return render(request,"patients/patient_list.html",{'page_obj':page_obj})

def patient_add(request):
    if request.method=="POST":
       form = PatientForm(request.POST)

       if form.is_valid():
          form.save()
          messages.success(request,"Patient added successfulyy")
          return redirect("patient_list")
    else:        
      form=PatientForm()
     
    return render(request,"Patients/patient_form.html",{"form":form})



def patient_edit(request,pk):
    patient=get_object_or_404(Patient,pk=pk)
    if request.method=="POST":
      form=PatientForm(request.POST,instance=patient)

      if form.is_valid():
         form.save()
         messages.success(request,"Patient details edited successfully")
         return redirect("patient_list")
    else:
       form=PatientForm(instance=patient)  
      
    return render(request,"Patients/patient_form.html",{"form":form}) 


def patient_delete(request,pk):
   patient=get_object_or_404(Patient,pk=pk)  
   if request.method=="POST":
      patient.delete()
      messages.success(request,"Patient deleted successfuly")
      return redirect("patient_list")
   return render(request,"patients/patient_confirm_delete.html",{"patient":patient})




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