from django.shortcuts import render,redirect, get_object_or_404
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


def appointment_edit(request,pk):
   appointment =get_object_or_404(Appointment,pk=pk)
   if request.method=="POST":
      form=AppointmentForm(request.POST,instance=appointment)
      if form.is_valid():
         form.save()
         return redirect("appointment_list")
      else:
         print(form.errors)

   else:
      form=AppointmentForm(instance=appointment)
   return render(request,"Appointments/appointment_form.html",{"form":form})  


def appointment_delete(request,pk):
   appointment=get_object_or_404(Appointment,pk=pk)
   if request.method=="POST":
      appointment.delete()
      return redirect("appointment_list")

   else:
      form=AppointmentForm(instance=appointment)
   return render(request,"Appointments/appointment_confirm_delete.html",{"appointment":appointment})   