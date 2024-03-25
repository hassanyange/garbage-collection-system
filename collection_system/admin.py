from django.contrib import admin
from .models import  Company, CustomerRequest, UserProfile, CompanyProfile

# Register your models here.

admin.site.register(Company)
admin.site.register(CustomerRequest)
admin.site.register(UserProfile)
