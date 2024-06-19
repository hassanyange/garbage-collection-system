from django.contrib import admin
from .models import  Company, CustomerRequest, UserProfile, CompanyProfile, District, Street, Ward, User,Payment

# Register your models here.

admin.site.register(Company)
admin.site.register(CustomerRequest)
admin.site.register(UserProfile)
admin.site.register(Ward)
admin.site.register(District)
admin.site.register(Street)
admin.site.register(Payment)

