from django.contrib import admin
from .models import LoanApplication
# Register your models here.

# Custom admin class for LoanApplication
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'loan_amount', 'interest_rate', 'loan_term', 'status', 'date_submitted')
    list_filter = ('status',)
    search_fields = ('user__username',)
    
    # Add custom actions for loan approval and rejection
    actions = ['approve_loans', 'reject_loans']
    
    def approve_loans(self, request, queryset):
        """Approve selected loans."""
        queryset.update(status='approved')
        self.message_user(request, "Selected loans have been approved.")
    
    def reject_loans(self, request, queryset):
        """Reject selected loans."""
        queryset.update(status='rejected')
        self.message_user(request, "Selected loans have been rejected.")
    
    approve_loans.short_description = "Approve selected loans"
    reject_loans.short_description = "Reject selected loans"

# Register the LoanApplication model with the customized admin
admin.site.register(LoanApplication, LoanApplicationAdmin)