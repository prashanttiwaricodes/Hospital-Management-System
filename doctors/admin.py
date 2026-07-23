from django.contrib import admin
from .models import Doctor     #from .models import Doctor

# Register your models here.
@admin.register(Doctor)    #This is a decorator ,they are cleaner,a modern way of registering a model with a custom admin class.
class DoctorAdmin(admin.ModelAdmin):   #this controls how the Docor model appears in the django admin.

    #with it you will see table data
    list_display=(
        "id",
        "name",
        "specialization",
        "email",
    )

    #Now django adds search box useful when there are 100s of doctors.
    search_fields=(
        "name",
        "specialization",
        "email",
    )

    #this creates filter on the right side click one and django shows only that specialization doctors.
    list_filter=(
        "specialization",
    )

    #this short doctors alphabeticaly
    ordering=(
        "name",
    )