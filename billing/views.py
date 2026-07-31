from django.shortcuts import render,redirect
from .models import Bill
from .forms import BillForm

# Create your views here.
def bills_list(request):
    bills=Bill.objects.all()
    context={
        "bills":bills
    }
    return render(request,"Billings/bills_list.html",context)


def bills_add(request):
    if request.method=="POST":
        form=BillForm(request.POST)
        if form.is_valid():
         form.save()
        return redirect("bills_list")
    else:
       form=BillForm()
    return render(request,"Billings/bill_form.html",{"form":form})           
    
