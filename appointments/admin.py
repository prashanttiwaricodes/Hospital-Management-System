from django.contrib import admin
from .models import Appointment

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=(
        "doctor",
        "patient",
        "appointment_date",
        "appointment_time",
        "reason",
        "status",
        "created_at",
    )


