from django.db import models
from django.contrib.auth.models import User

class GarbageCollectionRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)

class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=50)
    company_description = models.TextField()
    picture = models.ImageField (upload_to='static/images')

    def __str__(self):
        return self.company_name

    
class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=255, blank=True)
    types_of_garbage = models.TextField(max_length=255, blank=True)
    working_hours = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(max_length=100, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    picture = models.ImageField (upload_to='static/images')
    # Add more fields as needed
    
    def __str__(self):
        return self.name
    
class CustomerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    payment_status = models.BooleanField(default=False)    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username