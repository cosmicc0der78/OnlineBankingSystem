# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from banking.models import Account

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    contact_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Contact Number'}))
    account_type = forms.ChoiceField(choices=Account.ACCOUNT_TYPES, label="Account Type")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=4, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter OTP'}))

    def clean_otp(self):
        otp = self.cleaned_data.get('otp')
        if otp != '3773':  # Static OTP for demonstration
            raise forms.ValidationError("Invalid OTP.")
        return otp

# Form to update the User model (basic user info like username and email)
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # Allow user to update username and email

# Form to update the Profile model (extra profile info like contact number, address, etc.)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact_number', 'address', 'date_of_birth']  # Allow user to update contact, address, and DOB