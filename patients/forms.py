from django import forms
from .models import Patient

class PateintForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=[
            "name",
            "age",
            "gender",
            "blood_group",
            "phone",
            "address",

        ]