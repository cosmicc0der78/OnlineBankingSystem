# transactions/urls.py

from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('history/', views.transaction_history, name='transaction_history'),
    path('transfer/', views.initiate_transfer, name='initiate_transfer'),
]
