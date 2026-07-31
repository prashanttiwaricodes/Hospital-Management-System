from django.shortcuts import render,redirect,get_object_or_404
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


def bills_edit(request,pk):
    bill=get_object_or_404(Bill,pk=pk)
    if request.method=="POST":
        form=BillForm(request.POST,instance=bill)
        if form.is_valid():
         form.save()
        return redirect("bills_list")
    else:
       form=BillForm(instance=bill)
    return render(request,"Billings/bill_form.html",{"form":form})   


def bills_delete(request,pk):
   bill=get_object_or_404(Bill,pk=pk)
   if request.method=="POST":
      bill.delete()
      return redirect("bills_list")
   return render(request,"Billings/bill_confirm_delete.html",{"bill":bill})
    
