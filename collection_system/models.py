from django.db import models
from django.contrib.auth.models import User

class GarbageCollectionRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length= 255 , blank=True)
    picture = models.ImageField (upload_to='static/images')
    
class CustomerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    payment_status = models.BooleanField(default=False)    