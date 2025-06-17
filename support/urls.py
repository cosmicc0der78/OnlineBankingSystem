from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('submit/', views.submit_ticket, name='submit_ticket'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('my-tickets/', views.my_support_tickets, name='my_tickets'),
    path('notifications/', views.notifications, name='notifications'),
    path('mark-notifications-read/', views.mark_notifications_read, name='mark_notifications_read'),
]
