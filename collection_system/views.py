
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
from .models import CustomerRequest

@login_required
def home(request):
    # Logic to display home page
    return render(request, 'home.html')





def register_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company registered successfully!')
            return redirect('home')
    else:
        form = CompanyForm()
    return render(request, 'register_company.html', {'form': form})

@login_required

def make_request(request):
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save(commit=False)
            # Check if the user is authenticated
            if request.user.is_authenticated:
                request_obj.user = request.user
            else:
                # Handle the case of an unauthenticated user
                # For example, you can display an error message or redirect to another page
                messages.error(request, 'Please log in to make a request.')
                return redirect('home')  # Redirect the user to the home page
            request_obj.save()
            # Redirect to payment page after request is made
            return redirect('payment', request_obj.pk)
    else:
        # Check if it's an update operation and pass the instance to the form
        request_id = request.GET.get('request_id')
        if request_id:
            request_instance = get_object_or_404(CustomerRequest, pk=request_id)
            form = CustomerRequestForm(instance=request_instance)
        else:
            form = CustomerRequestForm()
    return render(request, 'make_request.html', {'form': form})


def payment(request, request_id):
    # Fetch the request object based on request_id
    request_obj = CustomerRequest.objects.get(pk=request_id)

    # Placeholder for payment processing logic
    if request.method == 'POST':
        # Add your payment processing logic here
        # For example:
        # if payment_is_successful:
        #     messages.success(request, 'Payment successful!')
        # else:
        #     messages.error(request, 'Payment failed. Please try again.')
        #     return redirect('payment', request_id=request_id)
        messages.success(request, 'Payment successful!')
        return redirect('home')  # Redirect to home page after successful payment

    return render(request, 'payment.html', {'request_obj': request_obj})

def company_detail(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    return render(request, 'company_detail.html', {'company': company})

def home(request):
    companies = Company.objects.all()
    return render(request, 'home.html', {'companies': companies})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        location = request.POST['location']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken.')
        else:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
            UserProfile.objects.create(user=user, location=location)
            messages.success(request, 'You have successfully registered!')
            return redirect('login')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')
