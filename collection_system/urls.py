from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register-company/', views.register_company, name='register_company'),
    path('make-request/', views.make_request, name='make_request'),
    path('payment/<int:request_id>/', views.payment, name='payment'),
    path('company/<int:company_id>/', views.company_detail, name='company_detail'),
]
