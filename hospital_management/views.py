from django.shortcuts import render ,redirect   
from doctors.models import Doctor
from patients.models import Patient
from appointments.models import Appointment
from billing.models import Bill
from prescriptions.models import Prescription
from departments.models import Department
import json
from datetime import date
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method=="POST":
        print("POST DATA:",request.POST)

        username=request.POST.get("username")
        password=request.POST.get("password")

        print("Username:",username)
        print("Password:",password)
      
        user=authenticate(request,username=username,password=password)
        print(user)

        if user is not None:
            login (request,user)
            return redirect("home")
            
        else:
         messages.error(request,"invalid username or password")
    return render(request,"login.html")


def logout_view(request):
   logout(request)
   messages.success(request,"Logged out successfully.")
   return redirect("login")


    
@login_required(login_url='login')
def home(request):   #This creates a function named home...Every django view recieves a request object
    doctor_count=Doctor.objects.count()
    patient_count=Patient.objects.count()
    appointment_count=Appointment.objects.count()
    bill_count=Bill.objects.count()
    prescription_count=Prescription.objects.count()
    department_count=Department.objects.count()
    today=date.today()
    context={
        
        "doctor_count":doctor_count,
        "patient_count":patient_count,
        "appointment_count":appointment_count,
        "bill_count":bill_count,
        "prescription_count":prescription_count,
        "department_count":department_count,
        "today":today,
    }
    return render(request,"home.html",context,)  #this means- take the incoming request, find home.html , Return it to browser 