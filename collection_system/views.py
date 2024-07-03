
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import CompanyForm, CustomerRequestForm, LoginForm, RegistrationForm
from .models import  CustomerRequest,Company
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import CustomerRequestForm
from .models import CustomerRequest, Payment
import uuid 



def make_request(request):
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save(commit=False)
            if request.user.is_authenticated:
                request_obj.user = request.user
            else:
                messages.error(request, 'Please log in to make a request.')
                return redirect('home')
            request_obj.save()
            return redirect('payment', request_id=request_obj.pk)
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        request_id = request.GET.get('request_id')
        if request_id:
            request_instance = get_object_or_404(CustomerRequest, pk=request_id)
            form = CustomerRequestForm(instance=request_instance)
        else:
            form = CustomerRequestForm()
    
    return render(request, 'make_request.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import CustomerRequest, Payment
import uuid

import random
import uuid

def payment(request, request_id):
    request_obj = get_object_or_404(CustomerRequest, pk=request_id)

    if request.method == 'POST':
        # Generate a unique transaction ID (example using UUID)
        transaction_id = uuid.uuid4().hex  # Generate a random UUID as transaction ID

        amount = request_obj.cost  # Assuming cost is a field on CustomerRequest

        # Generate a random control number
        control_number = random.randint(100000, 999999)

        try:
            # Create Payment object
            Payment.objects.create(
                transaction_id=transaction_id,
                payment_option=request.POST.get('payment_option'),
                payment_number=request.POST.get('payment_number'),  # Include this line
                amount=amount,
            )

            # Optionally, update CustomerRequest payment_status
            request_obj.payment_status = True
            request_obj.save()

            # Show a success message with the control number
            messages.success(request, f'Request submitted  successful!')
            return redirect('home')  # Redirect to the payment page

        except Exception as e:
            messages.error(request, f'Failed to process payment: {str(e)}')

    else:
        # Generate a control number when the payment page is initially loaded
        control_number = random.randint(100000, 999999)

    return render(request, 'payment.html', {'request_obj': request_obj, 'control_number': control_number})



def company_detail(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    return render(request, 'company_detail.html', {'company': company})


@login_required
def home(request):
    companies = Company.objects.all()
    return render(request, 'home.html', {'companies': companies})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                return redirect('home')  # Redirect to home page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


from django.shortcuts import redirect


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            form.save()
            messages.success(request, 'You have successfully registered!')
=======
            user = form.save()
            messages.success(request, ' You have successfully registered!')
>>>>>>> 35c7a7187ecc5c0a77540f514bfef15a6f8233b8
            return redirect('login')  # Redirect to login page after successful registration
        else:
            messages.error(request, 'There was an error with your registration')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')
