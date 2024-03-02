# collection_system/forms.py

from django import forms
from .models import Company, CustomerRequest

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location']

class CustomerRequestForm(forms.ModelForm):
    class Meta:
        model = CustomerRequest
        fields = ['location', 'name', 'phone_number']
