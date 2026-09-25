from django.contrib import admin
from .models import Ticket, TicketActivity


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
        'age',
        'overdue',
    )

    def age(self, obj):
        return obj.age_hours

    age.short_description = 'Age (hours)'

    def overdue(self, obj):
        return obj.is_overdue

    overdue.boolean = True
    overdue.short_description = 'Overdue'

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
@admin.register(TicketActivity)
class TicketActivityAdmin(admin.ModelAdmin):
      list_display = (
        'id',
        'ticket',
        'action',
        'description',
        'created_at',
    )

      list_filter = (
        'action',
        'created_at',
    )

      search_fields = (
        'ticket__subject',
        'action',
        'description',
    )