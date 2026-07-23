from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):  #create a form using the Doctor model.

    class Meta:  #meta class tells django how to build the form
        model=Doctor    #build this form using the Doctor model.
        fields=[
            "name",
            "specialization",
            "email",
            "phone",
        ]