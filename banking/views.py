# banking/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Account
from django.contrib import messages
from .forms import DepositForm, WithdrawalForm  # Forms for deposit and withdrawal

@login_required
def view_balance(request):
    # Assuming you have a way to get the current user and their associated account
    try:
        account = Account.objects.get(user=request.user)  # Adjust based on your logic
        return render(request, 'banking/view_balance.html', {'account': account})
    except Account.DoesNotExist:
        return render(request, 'banking/no_account.html')  # This is where the error occurred
    
@login_required
def deposit(request):
    account = Account.objects.get(user=request.user)
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            account.deposit(amount)
            return redirect('banking:view_balance')
    else:
        form = DepositForm()
    return render(request, 'banking/deposit.html', {'form': form})

@login_required
def withdraw(request):
    account = Account.objects.get(user=request.user)
    if request.method == 'POST':
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if account.withdraw(amount):
                return redirect('banking:view_balance')
            else:
                return HttpResponse("Insufficient funds", status=400)
    else:
        form = WithdrawalForm()
    return render(request, 'banking/withdraw.html', {'form': form})