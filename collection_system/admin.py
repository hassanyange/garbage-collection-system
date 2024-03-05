from django.contrib import admin
from .models import GarbageCollectionRequest, Company, CustomerRequest, UserProfile

# Register your models here.

admin.site.register(GarbageCollectionRequest)
admin.site.register(Company)
admin.site.register(CustomerRequest)
admin.site.register(UserProfile)