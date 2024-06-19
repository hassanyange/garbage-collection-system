from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone

class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=50)
    company_description = models.TextField()
    picture = models.ImageField(upload_to='images/')  # Adjusted upload_to path

    def __str__(self):
        return self.company_name


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # Removed max_length for TextField
    types_of_garbage = models.TextField(blank=True)
    working_hours = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(max_length=100, blank=True)
    contact_phone = models.CharField(max_length=10, blank=True, validators=[RegexValidator(r'^\d{10}$', 'Enter a 10-digit phone number.')])
    picture = models.ImageField(upload_to='images/')  # Adjusted upload_to path

    def __str__(self):
        return self.name


class CustomerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, blank=True, validators=[RegexValidator(r'^\d{10}$', 'Enter a 10-digit phone number.')])
    district = models.ForeignKey('District', on_delete=models.CASCADE, null=True, blank=True)
    ward = models.ForeignKey('Ward', on_delete=models.CASCADE, null=True, blank=True)
    street = models.ForeignKey('Street', on_delete=models.CASCADE, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)  # Example cost field
    payment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)  # Changed to auto_now for automatic updates

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class District(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ward(models.Model):
    ward_name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.ward_name


class Street(models.Model):
    street_name = models.CharField(max_length=255)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.street_name


class Payment(models.Model):
    transaction_id = models.CharField(max_length=100)
    payment_option = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment #{self.id} - {self.transaction_id}"
