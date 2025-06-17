from django.urls import path
from . import views

app_name = 'accounts'  # This defines the namespace for this app

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),  # Define 'home' URL
    path('profile/', views.profile_view, name='profile'),  # URL for viewing the profile
    path('profile/edit/', views.profile_edit, name='profile_edit'),  # URL for editing the profile]
]