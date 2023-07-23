from django.db import models

# Create your models here.

class Contactinfo(models.Model):
    fullname = models.CharField(max_length=200)
    phone =   models.CharField(max_length=50)
    email =   models.CharField(max_length=300)
    meg   =  models.TextField(max_length=1000)
    location =  models.CharField(max_length=100)
    subject = models.CharField(max_length=200, default=1)
    
    
    def __str__(self):
        return self.fullname