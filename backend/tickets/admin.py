from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'subject',
        'student',
        'category',
        'priority',
        'status',
        'assigned_to',
    )

    list_filter = (
        'category',
        'priority',
        'status',
    )

    search_fields = (
        'subject',
        'description',
        'student__username',
        'student__email',
    )