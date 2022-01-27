from django.db import models
from django.contrib.auth.models import User
from user.models import MyUser

# Create your models here.


class Medications(models.Model):
    name = models.CharField(max_length=20)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default= 0)
    dosage = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    