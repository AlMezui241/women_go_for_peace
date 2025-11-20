# donations/urls.py
from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [
    path('', views.DonationView.as_view(), name='donate'),
    path('success/<int:donation_id>/', views.donation_success, name='success'),
]