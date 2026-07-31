from django.db import models
from patients.models import Patient

# Create your models here.
class Bill(models.Model):
    PAYMENT_STATUS=[("Paid","Paid"),
                    ("Pending","Pending"),
                   ]
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_status=models.CharField(max_length=20,choices=PAYMENT_STATUS,default="Pending")
    bill_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.patient.name}- ₹{self.amount}"

