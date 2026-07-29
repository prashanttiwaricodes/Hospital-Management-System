from django.db import models
from doctors.models import Doctor
from patients.models import Patient

# Create your models here.

class Appointment(models.Model):
    STATUS_CHOICES=[
        ("Pending","Pending"),
        ("Completed","Completed"),
        ("Cancelled","Cancelled"),
    ]
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()
    reason=models.TextField()
    status=models.CharField(max_length=25,choices=STATUS_CHOICES,default="Pending")
    created_at=models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f"{self.patient.name}-{self.doctor.name}"  
