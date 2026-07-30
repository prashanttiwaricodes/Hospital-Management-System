from django.shortcuts import render,redirect
from .models import Appointment
from .forms import AppointmentForm

# Create your views here.
def appointment_list(request):
    appointments=Appointment.objects.all()

    context= {
        "appointments": appointments
    }

    return render(request,"Appointments/appointment_list.html",context)



def appointment_add(request):
    if request.method=="POST":
        form=AppointmentForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("appointment_list")
        else:
           print(form.errors)

    else:    
     form=AppointmentForm()

    return render(request,"Appointments/appointment_form.html",{"form":form})

    
