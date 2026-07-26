from django.shortcuts import render
from .models import Patient
from .forms import PateintForm

# Create your views here.
def patient_list(request):
    patients=Patient.objects.all()

    context={
        "patients":patients
    }

    return render(request,"patients/patient_list.html",context)

