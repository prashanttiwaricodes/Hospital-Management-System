from django.shortcuts import render
from .models import Prescription

# Create your views here.
def prescription_list(request):
    prescriptions=Prescription.objects.all()

    context={
        "prescriptions":prescriptions
    }

    return render(request,"Prescriptions/prescription_list.html",context)


def prescription_add(request):
    pass   
