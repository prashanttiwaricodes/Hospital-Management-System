from django.shortcuts import render,redirect,get_object_or_404
from .models import Patient
from .forms import PatientForm

# Create your views here.
def patient_list(request):
    patients=Patient.objects.all()

    context={
        "patients":patients
    }

    return render(request,"patients/patient_list.html",context)

def patient_add(request):
    if request.method=="POST":
       form = PatientForm(request.POST)

       if form.is_valid():
          form.save()
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
         return redirect("patient_list")
    else:
       form=PatientForm(instance=patient)  
    return render(request,"Patients/patient_form.html",{"form":form}) 


def patient_delete(request,pk):
   patient=get_object_or_404(Patient,pk=pk)  
   if request.method=="POST":
      patient.delete()
      return redirect("patient_list")
   return render(request,"patients/patient_confirm_delete.html",{"patient":patient})