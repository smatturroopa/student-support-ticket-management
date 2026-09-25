from datetime import timedelta
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Ticket(models.Model):

    CATEGORY_CHOICES = [
        ('ACADEMIC', 'Academic'),
        ('TECHNICAL', 'Technical'),
        ('FINANCIAL', 'Financial'),
        ('ADMINISTRATIVE', 'Administrative'),
        ('OTHER', 'Other'),
    ]
    PRIORITY_CHOICES = [
    ('LOW', 'Low'),
    ('MEDIUM', 'Medium'),
    ('HIGH', 'High'),
    ('URGENT', 'Urgent'),
]

    SLA_HOURS = {
    'LOW': 72,
    'MEDIUM': 48,
    'HIGH': 24,
    'URGENT': 8,
}

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('PENDING', 'Pending'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student_tickets'
    )

    subject = models.CharField(max_length=200)

    description = models.TextField()

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='OTHER'
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='MEDIUM'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tickets'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    sla_due_at = models.DateTimeField(
        null=True,
        blank=True
    )

    resolved_at = models.DateTimeField(
        null=True,
        blank=True
    )

    resolution_notes = models.TextField(
        blank=True
    )

    escalated = models.BooleanField(
        default=False
    )

    pending_reason = models.TextField(
        blank=True
    )

    def save(self, *args, **kwargs):
      is_new = self.pk is None
      old_status = None
      old_assigned_to = None

      if not is_new:
        old_ticket = Ticket.objects.get(pk=self.pk)
        old_status = old_ticket.status
        old_assigned_to = old_ticket.assigned_to

      if not self.sla_due_at:
        hours = self.SLA_HOURS.get(self.priority, 48)
        self.sla_due_at = timezone.now() + timedelta(hours=hours)

        super().save(*args, **kwargs)

      if is_new:
         TicketActivity.objects.create(
            ticket=self,
            action='Ticket Created',
            description='Ticket was created'
        )

      if not is_new and old_status != self.status:
        TicketActivity.objects.create(
            ticket=self,
            action='Status Changed',
            description=f'Status changed from {old_status} to {self.status}'
        )
      if self.status == 'PENDING':
         TicketActivity.objects.create(
            ticket=self,
            action='Ticket Pending',
            description=f'Ticket moved to pending. Reason: {self.pending_reason}'
        )

      if self.status == 'RESOLVED':
         TicketActivity.objects.create(
                ticket=self,
                action='Ticket Resolved',
                description='Ticket was resolved'
            )

      if not is_new and old_assigned_to != self.assigned_to:
         TicketActivity.objects.create(
            ticket=self,
            action='Assignment Changed',
            description=f'Assigned to {self.assigned_to}'
        )
    @property
    def is_overdue(self): 
        return self.sla_due_at and timezone.now() > self.sla_due_at
    @property
    def age_hours(self):
        return round((timezone.now() - self.created_at).total_seconds() / 3600, 2)
class TicketActivity(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='activities'
    )
    action = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticket} - {self.action}"