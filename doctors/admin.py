from django.contrib import admin
from .models import Doctor     #from .models import Doctor

# Register your models here.
admin.site.register(Doctor)     #by registering the model your are telling django : Shoe the Doctor model in admin .
