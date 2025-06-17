from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import LoanApplication
from .forms import LoanApplicationForm
from django.http import HttpResponse

@login_required
def loan_application(request):
    """Loan application form view."""
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            loan_application = form.save(commit=False)
            loan_application.user = request.user  # Associate the application with the logged-in user
            loan_application.save()
            return redirect('loans:loan_list')  # Redirect to the loan list page
    else:
        form = LoanApplicationForm()

    return render(request, 'loans/loan_application.html', {'form': form})

@login_required
def loan_list(request):
    """View to list all loan applications of the logged-in user."""
    loans = LoanApplication.objects.filter(user=request.user)
    return render(request, 'loans/loan_list.html', {'loans': loans})

# Check if the user is an admin
def is_admin(user):
    return user.is_staff  # Only admin users have `is_staff` set to True

@login_required
@user_passes_test(is_admin)  # Ensures only admins can access this view
def admin_loan_approval(request, loan_id):
    """Admin view to approve or reject loan applications."""
    loan = LoanApplication.objects.get(id=loan_id)

    # Check if the loan is pending, so that only pending loans can be approved or rejected
    if loan.status == 'pending':
        if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'approve':
                loan.status = 'approved'  # Approve the loan
            elif action == 'reject':
                loan.status = 'rejected'  # Reject the loan
            loan.save()
            return redirect('loans:loan_list')  # Redirect to the loan list view after action
    else:
        return HttpResponse("Invalid loan status", status=400)  # Return error if status is not 'pending'

    return render(request, 'loans/admin_loan_approval.html', {'loan': loan})