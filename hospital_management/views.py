from django.shortcuts import render   # render() is a django shortcut that loads an html template and returns it as a response ...without render() Django woudnot know how to display html page
from doctors.models import Doctor
from patients.models import Patient
from appointments.models import Appointment
from billing.models import Bill
from prescriptions.models import Prescription
from departments.models import Department

def home(request):   #This creates a function named home...Every django view recieves a request object
    doctor_count=Doctor.objects.count()
    patient_count=Patient.objects.count()
    appointment_count=Appointment.objects.count()
    bill_count=Bill.objects.count()
    prescription_count=Prescription.objects.count()
    department_count=Department.objects.count()

    context={
        "doctor_count":doctor_count,
        "patient_count":patient_count,
        "appointment_count":appointment_count,
        "bill_count":bill_count,
        "prescription_count":prescription_count,
        "department_count":department_count,
    }
    return render(request,"home.html",context)  #this means- take the incoming request, find home.html , Return it to browser 