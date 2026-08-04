from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from .forms import DepartmentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required
def department_list(request):
    department=Department.objects.all().order_by("id")
    paginator=Paginator(department,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
   

    return render(request,"Department/department_list.html",{"page_obj":page_obj})



def department_add(request):
    if request.method=="POST":
        form=DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," New Department added")
            return redirect("department_list")
    else:
        form=DepartmentForm()
    return render(request,"Department/department_form.html",{"form":form})       




def department_edit(request,pk):
    department=get_object_or_404(Department,pk=pk)
    if request.method=="POST":
        form=DepartmentForm(request.POST,instance=department)
        if form.is_valid():
            form.save()
            messages.success(request,"department edited successfully")
            return redirect("department_list")
    else:
        form=DepartmentForm(instance=department)
    return render(request,"Department/department_form.html",{"form":form})  



def department_delete(request,pk):
    department=get_object_or_404(Department,pk=pk)
    if request.method=="POST":
        department.delete()
        messages.success(request,"Department Deleted")
        return redirect("department_list")
    return render(request,"Department/department_confirm_delete.html",{"department":department})