from django.db import models
from appointments.models import Appointment

# Create your models here.
class Prescription(models.Model):
    appointment=models.ForeignKey(Appointment,on_delete=models.CASCADE)
    diagnosis=models.TextField()
    medicines=models.TextField()
    dosage=models.CharField(max_length=200)
    instructions=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f"Prescription #{self.id}"   
