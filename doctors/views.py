from django.shortcuts import render,redirect,get_object_or_404
from .models import Doctor  #we are importing Doctor model without this we cannot access databse table
from .forms import DoctorForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages




# Create your views here.



@login_required
def doctor_list(request):
    search=request.GET.get("search")
    doctors=Doctor.objects.all().order_by('id')  #give me all doctors from the database 

    if search:
       doctors=doctors.filter(name__icontains=search)

    paginator=Paginator(doctors,5)  # 5 doctors per page
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    return render(request,"doctors/doctor_list.html",{'page_obj':page_obj})   #this means open the template ,send the doctors, display them 
                  

def doctor_add(request):
    if request.method =="POST":
        form=DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"New doctor added successfully")
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
         messages.success(request,"Successfully Edit the Details")
         return redirect("doctor_list")
   else:
      form= DoctorForm(instance=doctor)
     
   return render(request,"doctors/doctor_form.html",{"form":form})
   



def doctor_delete(request,pk):
   doctor=get_object_or_404(Doctor,pk=pk)
   if request.method=="POST":
      doctor.delete()
      messages.success(request,"Deleted Successfully")
      return redirect("doctor_list")

   return render(request,"doctors/doctor_confirm_delete.html",{"doctor":doctor})








