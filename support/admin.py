from django.contrib import admin
from .models import SupportTicket

class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'subject')
    actions = ['mark_in_progress', 'close_tickets']
    
    # Allow response field to be editable
    fields = ('user', 'subject', 'description', 'status', 'response', 'created_at', 'updated_at')
    readonly_fields = ('user', 'created_at', 'updated_at')
    
    def mark_in_progress(self, request, queryset):
        queryset.update(status='in_progress')
        self.message_user(request, "Selected tickets have been marked as In Progress.")
    
    def close_tickets(self, request, queryset):
        queryset.update(status='closed')
        self.message_user(request, "Selected tickets have been closed.")
    
    mark_in_progress.short_description = "Mark selected tickets as In Progress"
    close_tickets.short_description = "Close selected tickets"

admin.site.register(SupportTicket, SupportTicketAdmin)
