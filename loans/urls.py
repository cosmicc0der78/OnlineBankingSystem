from django.urls import path
from . import views

app_name = 'loans'

urlpatterns = [
    path('apply/', views.loan_application, name='loan_application'),
    path('loan_list/', views.loan_list, name='loan_list'),
    path('admin/approve/<int:loan_id>/', views.admin_loan_approval, name='admin_loan_approval'),
]
