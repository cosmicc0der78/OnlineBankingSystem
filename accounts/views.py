from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Profile
from banking.models import Account
from support.models import Notification  # Import Notification model


from .forms import LoginForm, RegisterForm, OTPForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse  # Import reverse to handle URL resolution
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    account = request.user.account  # or however you get the account info
    context = {
        'account': account,
        # other context variables
    }
    return render(request, 'accounts/home.html', context)


def login_view(request):
    if request.method == 'POST':
        if 'otp' in request.POST:  # Check if we're in the OTP stage
            otp_form = OTPForm(request.POST)
            if otp_form.is_valid():
                user_id = request.session.get('user_id')
                if user_id:
                    user = User.objects.get(pk=user_id)  # Retrieve the user from the database
                    login(request, user)  # Log in the user
                    del request.session['user_id']  # Clear the session after login
                    return redirect('accounts:home')
                else:
                    messages.error(request, "Session expired. Please log in again.")
                    return redirect('accounts:login')
            else:
                messages.error(request, "Invalid OTP.")
                return render(request, 'accounts/login.html', {'otp_form': otp_form})

        else:  # First stage - check username and password
            login_form = LoginForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                request.session['user_id'] = user.pk  # Save user ID in session
                messages.info(request, "OTP sent to email. Please enter OTP.")
                return render(request, 'accounts/login.html', {'otp_form': OTPForm()})
            else:
                messages.error(request, 'Invalid username or password.')
        
        return redirect(reverse('accounts:home'))  # Use namespace if needed
    else:
        login_form = LoginForm()
    return render(request, 'accounts/login.html', {'login_form': login_form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Save the User without committing to add additional details later
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save the User to the database

            # Check if the user already has a profile
            if not Profile.objects.filter(user=user).exists():
                # Create a Profile with the contact number provided in the form
                contact_number = form.cleaned_data['contact_number']
                Profile.objects.create(user=user, contact_number=contact_number)

            # Get the account type from the form and create the Account
            account_type = form.cleaned_data['account_type']
            Account.objects.create(user=user, balance=0.0, account_type=account_type)

            # Log the user in automatically after registration
            login(request, user)
            return redirect('accounts:login')  # Redirect to the user's home page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

# View to display the user profile
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')  # Renders the profile.html template

@login_required
def profile_edit(request):
    # If the request method is POST, it means the user is submitting the form to update the profile
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Save the updated user info
            profile_form.save()  # Save the updated profile info
            messages.success(request, 'Your profile has been updated!')
            return redirect('accounts:profile')  # Redirect to profile view after successful update
    
    else:
        # If it's a GET request, pre-populate the forms with the current user's data
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'accounts/profile_edit.html', context)

# Home view for logged-in users
@login_required
def home_view(request):
    # Retrieve the user's account
    try:
        account = Account.objects.get(user=request.user)
    except Account.DoesNotExist:
        account = None  # Handle the case if the account doesn't exist

    # Get the count of unread notifications
    unread_count = Notification.objects.filter(user=request.user, is_read=False).count()

    # Pass the account and unread_count to the template
    return render(request, 'accounts/home.html', {'account': account, 'unread_count': unread_count})