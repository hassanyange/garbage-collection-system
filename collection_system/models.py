from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



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
    contact_phone = models.CharField(max_length=10, blank=True, validators=[RegexValidator(r'^\d{10}$', 'Enter a 10-digit phone number.')])
    picture = models.ImageField(upload_to='static/images')
    background_image = models.ImageField(upload_to='static/images', default='yange.jpg')  # New field for background image

    def __str__(self):
        return self.name

    
class CustomerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, blank=True, validators=[RegexValidator(r'^\d{10}$', 'Enter a 10-digit phone number.')])
    picture = models.ImageField(upload_to='static/images', default='yange.jpg')
    payment_status = models.BooleanField(default=False)   

    def __str__(self) :
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username