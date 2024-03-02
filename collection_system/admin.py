from django.contrib import admin
from .models import GarbageCollectionRequest, Company, CustomerRequest

# Register your models here.

admin.site.register(GarbageCollectionRequest)
admin.site.register(Company)
admin.site.register(CustomerRequest)