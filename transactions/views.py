from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Transaction
from .forms import TransferForm
from django.db.models import Q

@login_required
def transaction_history(request):
    user = request.user  # Get the logged-in user

    # Get the transaction history for the logged-in user (both sent and received)
    transactions = Transaction.objects.filter(
        Q(from_user=user) | Q(to_user=user)
    ).order_by('-timestamp')  # Order by timestamp to show latest transactions first

    return render(request, 'transactions/transaction_history.html', {'transactions': transactions})

@login_required
def initiate_transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            to_user = form.cleaned_data['to_account']
            amount = form.cleaned_data['amount']
            
            # Check if user has enough balance (assuming user's balance is a property on profile)
            if request.user.account.balance >= amount:
                # Create the transaction
                Transaction.objects.create(
                    from_user=request.user, 
                    to_user=to_user, 
                    amount=amount, 
                    transaction_type='transfer'
                )
                # Update balances
                request.user.account.balance -= amount
                request.user.account.save()
                to_user.account.balance += amount
                to_user.account.save()
                
                messages.success(request, f'Transferred ${amount} to {to_user.username}')
                return redirect('transactions:transaction_history')
            else:
                messages.error(request, 'Insufficient funds for this transfer.')
    else:
        form = TransferForm()
    return render(request, 'transactions/initiate_transfer.html', {'form': form})
