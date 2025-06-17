# banking/urls.py
from django.urls import path
from . import views

app_name = 'banking'

urlpatterns = [
    path('balance/', views.view_balance, name='view_balance'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
]
