

from django import forms
from .models import Company, CustomerRequest, UserProfile, User, Ward, District, Street
from django.contrib.auth.forms import UserCreationForm
import re
from django import forms
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    if not re.match(r'^[0-9]{10}$', value):
        raise ValidationError('Phone number must be 10 digits.')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    location = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[validate_password]
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'location']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        try:
            validate_password(password1)
        except ValidationError as e:
            raise forms.ValidationError(e)
        return password2

        
class CustomerRequestForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label="Select District")
    ward = forms.ModelChoiceField(queryset=Ward.objects.all(), empty_label="Select Ward")
    street = forms.ModelChoiceField(queryset=Street.objects.all(), empty_label="Select Street")
    phone_number = forms.CharField(
        max_length=10,
        validators=[validate_phone_number],
        help_text='Enter a 10-digit phone number'
    )

    class Meta:
        model = CustomerRequest
        fields = ['name', 'phone_number', 'district', 'ward', 'street']

    def clean(self):
        cleaned_data = super().clean()
        district = cleaned_data.get('district')
        ward = cleaned_data.get('ward')
        street = cleaned_data.get('street')

        if district and ward and street:
            if ward.district != district:
                raise forms.ValidationError("The selected ward does not belong to the selected district.")
            if street.ward != ward:
                raise forms.ValidationError("The selected street does not belong to the selected ward.")
        
        return cleaned_data

        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['location'] 


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']