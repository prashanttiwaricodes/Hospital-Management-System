from django.shortcuts import render, redirect, get_object_or_404
from .models import Prescription
from .forms import PrescriptionForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

@login_required
def prescription_list(request):
    prescriptions=Prescription.objects.all().order_by("id")
    paginator=Paginator(prescriptions,5)

    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

   

    return render(request,"Prescriptions/prescription_list.html",{"page_obj":page_obj})


def prescription_add(request):
    if request.method=="POST":
        form=PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," New Prescriptions added successfully")
            return redirect("prescription_list")
    else:
        form=PrescriptionForm()
    return render(request,"Prescriptions/prescription_form.html",{"form":form}) 


def prescription_edit(request,pk):
    prescription=get_object_or_404(Prescription,pk=pk)
    if request.method=="POST":
        form=PrescriptionForm(request.POST,instance=prescription)
        if form.is_valid():
            form.save()
            messages.success(request,"Prescriptions edited successfully")
            return redirect("prescription_list")
    else:
        form=PrescriptionForm(instance=prescription)
    return render(request,"Prescriptions/prescription_form.html",{"form":form})    



def prescription_delete(request,pk):
    prescription=get_object_or_404(Prescription,pk=pk)
    if request.method=="POST":
        prescription.delete()
        messages.success(request,"Presciption deleted successfully")
        return redirect("prescription_list")
    return render(request,"Prescriptions/prescription_confirm_delete.html",{"prescription":prescription})    
    

    

