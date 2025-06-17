# banking/urls.py
from django.urls import path
from . import views

app_name = 'banking'

urlpatterns = [
    path('balance/', views.view_balance, name='view_balance'),
]
