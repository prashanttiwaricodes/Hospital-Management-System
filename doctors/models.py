from django.db import models   
# without importing models django wont able to create table.
# after creating class run migration and migrate on cmd prompt 

# Create your models here.
class Doctor(models.Model):    # Django creates a database table Doctor name.
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=12)

    def __str__(self):     #yeh current object ko print krta h withot this you will see doctor object 1
        return self.name
    

