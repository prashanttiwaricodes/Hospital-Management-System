from django.shortcuts import render, redirect
from .models import Department
from .forms import DepartmentForm

# Create your views here.
def department_list(request):
    department=Department.objects.all()
    context={
        "departments":department
    }

    return render(request,"Department/department_list.html",context)



def department_add(request):
    if request.method=="POST":
        form=DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("department_list")
    else:
        form=DepartmentForm()
    return render(request,"Department/department_form.html",{"form":form})        