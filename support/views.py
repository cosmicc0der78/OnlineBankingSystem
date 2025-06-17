from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SupportTicketForm
from .models import SupportTicket, Notification
from django.contrib import messages
from django.shortcuts import redirect

@login_required
def submit_ticket(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # Associate the ticket with the logged-in user
            ticket.save()
            messages.success(request, "Your support ticket has been submitted successfully!")  # Success message
            return redirect('accounts:home')  # Redirect to the homepage or any other page
    else:
        form = SupportTicketForm()
    return render(request, 'support/submit_ticket.html', {'form': form})

def is_admin(user):
    return user.is_staff  # Only allow access if the user is an admin

@login_required
@user_passes_test(is_admin, login_url='accounts:home')  # Redirect non-admin users
def ticket_list(request):
    tickets = SupportTicket.objects.all()
    return render(request, 'support/ticket_list.html', {'tickets': tickets})

@login_required
@user_passes_test(is_admin, login_url='accounts:home')
def ticket_detail(request, ticket_id):
    ticket = SupportTicket.objects.get(id=ticket_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'mark_in_progress':
            ticket.status = 'in_progress'
            # Create a notification for the user
            Notification.objects.create(
                user=ticket.user,
                message=f"Your support ticket '{ticket.subject}' is now in progress."
            )
        elif action == 'close':
            ticket.status = 'closed'
            Notification.objects.create(
                user=ticket.user,
                message=f"Your support ticket '{ticket.subject}' has been closed."
            )
        ticket.save()
        return redirect('support:ticket_list')
    return render(request, 'support/ticket_detail.html', {'ticket': ticket})

@login_required
def my_support_tickets(request):
    # Fetch tickets submitted by the logged-in user
    tickets = SupportTicket.objects.filter(user=request.user)
    return render(request, 'support/my_tickets.html', {'tickets': tickets})

@login_required
def notifications(request):
    notifications = request.user.notifications.filter(is_read=False)
    return render(request, 'support/notifications.html', {'notifications': notifications})

@login_required
def mark_notifications_read(request):
    # Check if the request method is POST to ensure the form submission is intentional
    if request.method == 'POST':
        request.user.notifications.filter(is_read=False).update(is_read=True)
        messages.success(request, "All notifications marked as read.")
    return redirect('support:notifications')