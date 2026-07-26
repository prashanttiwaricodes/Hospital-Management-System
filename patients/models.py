from django.db import models

# Create your models here.
class Patient(models.Model):
    BLOOD_GROUPS=[
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-'),
    ]
    GENDER_CHOICES=[
        ('Male','Male'),
        ('Feamale','Female'),
        ('Other','Other'),
    ]
    name=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    blood_group=models.CharField(max_length=3,choices=BLOOD_GROUPS)
    phone=models.CharField(max_length=15)
    address=models.TextField()

    def __str__(self):
        return self.name
