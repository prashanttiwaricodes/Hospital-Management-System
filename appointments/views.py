from django.shortcuts import render
from .models import Appointment

# Create your views here.
def appointment_list(request):
    appointment=Appointment.objects.all()
    
