from django.contrib import admin
from .models import Doctor     #from .models import Doctor

# Register your models here.
@admin.register(Doctor)    #by registering the model your are telling django : Shoe the Doctor model in admin .
class DoctorAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "name",
        "specialization",
        "email",
    )
    search_fields=(
        "name",
        "specialization",
        "email",
    )
    list_filter=(
        "specialization",
    )
    ordering=(
        "name",
    )