"""
URL configuration for hospital_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include   # adding include means-if we right every url inside one file it becomes huge , instead every app manages its own url this keeps project modular.
from .views import home     # we are importing home() function because it is in another file (views.py), if we dont import it urls.py doesnt know what home is

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),  # ""-root url (http://127.0.0.1:8000/)  home-this is the function we created in views.py... when this URL is visited,Django executes  name="home"- this gives route a name ..later instead of writing URLs directly in HTML, we will use {% home %}
    path("doctors/",include("doctors.urls")),
]
