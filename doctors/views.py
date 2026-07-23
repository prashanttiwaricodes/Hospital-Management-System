from django.shortcuts import render
from .models import Doctor  #we are importing Doctor model without this we cannot access databse table
from .forms import DoctorForm
# Create your views here.
def doctor_list(request):
    doctors=Doctor.objects.all()  #give me all doctors from the database 

    context={
        "doctors":doctors   # think  of as a parcel .. packing the data
    }

    return render(request,"doctors/doctor_list.html",context   #this means open the template ,send the doctors, display them 
                  )

def doctor_add(request):

    form=DoctorForm()
    return render(
        request,"doctors/doctor_form.html",{"form":form}
    )


    