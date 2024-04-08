from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.login_view, name='login'),  # Set login view as the default landing page
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home, name='home'), 
    path('make-request/', views.make_request, name='make_request'),
    path('payment/<int:request_id>/', views.payment, name='payment'),
    path('company/<int:company_id>/', views.company_detail, name='company_detail'),
    path('logout/', views.logout_view, name='logout'),

    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]

