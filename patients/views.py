from django.shortcuts import render,redirect
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