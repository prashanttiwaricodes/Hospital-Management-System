from django.shortcuts import render,redirect,get_object_or_404
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
    if request.method =="POST":
        form=DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("doctor_list")
    else:
     form=DoctorForm()
    return render(
        request,"doctors/doctor_form.html",{"form":form}
    )

def doctor_edit(request,pk):
   doctor=get_object_or_404(Doctor,pk=pk)
   if request.method=="POST":
      form=DoctorForm(request.POST,instance=doctor)

      if form.is_valid():
         form.save()
         return redirect("doctor_list")
   else:
      form= DoctorForm(instance=doctor)
   return render(request,"doctors/doctor_form.html",{"form":form})
   



def doctor_delete(request,pk):
   doctor=get_object_or_404(Doctor,pk=pk)
   if request.method=="POST":
      doctor.delete()
      return redirect("doctor_list")

   return render(request,"doctors/doctor_confirm_delete.html",{"doctor":doctor})


    