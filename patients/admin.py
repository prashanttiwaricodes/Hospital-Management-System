from django.contrib import admin
from .models import Patient

# Register your models here.
@admin.register(Patient)
class PateintAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "age",
        "gender",
        "blood_group",
        "phone",
        "address",
    )

    search_fields=(
        "name",
        "blood_group",
        "phone",
    )

    list_filter=(
        "blood_group",
    )

    ordering=(
        "name",
    )

