

from django import forms
from .models import Company, CustomerRequest, UserProfile, User, Ward, District, Street
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location']

from django import forms
from .models import CustomerRequest, District, Ward, Street

class CustomerRequestForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label="Select District")
    ward = forms.ModelChoiceField(queryset=Ward.objects.all(), empty_label="Select Ward")
    street = forms.ModelChoiceField(queryset=Street.objects.all(), empty_label="Select Street")

    class Meta:
        model = CustomerRequest
        fields = ['name', 'phone_number', 'district', 'ward', 'street']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['ward'].queryset = Ward.objects.filter(district=self.instance.district)
            self.fields['street'].queryset = Street.objects.filter(ward=self.instance.ward)

        
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    location = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'location']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['location'] 
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']