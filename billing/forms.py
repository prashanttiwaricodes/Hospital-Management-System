from django import forms
from .models import Bill

class BillForm(forms.ModelForm):
    class Meta:
        model=Bill
        fields=[
            "patient",
            "amount",
            "payment_status",
            "bill_date"

        ] 

        widgets={
            "bill_date":forms.DateInput(attrs={"type":"date"}),
        }