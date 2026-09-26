# Student Support & Ticket Management System
## Overview

A Django-based Student Support and Ticket Management System designed to help students raise support requests and allow staff to manage, assign, prioritize, track, and resolve those requests.

The system supports ticket lifecycle management, SLA tracking, ticket ageing, overdue detection, escalation, resolution tracking, and activity history.
## Features

- Student, Staff, and Admin roles
- Create and manage support tickets
- Ticket categories
- Ticket priority management
- Ticket status management
- Assign tickets to staff
- Pending ticket handling with pending reason
- SLA due-time calculation based on priority
- Ticket ageing in hours
- Overdue ticket detection
- Automatic escalation for overdue tickets
- Resolution notes and resolution timestamp
- Ticket activity/history tracking
- Status change history
- Assignment change history
- Django Admin search and filtering
## Ticket Workflow

```text
OPEN
  ↓
IN_PROGRESS
  ↓
PENDING
  ↓
IN_PROGRESS
  ↓
RESOLVED
  ↓
CLOSED

## Priority Levels

| Priority | SLA |
|----------|-----|
| LOW | 72 hours |
| MEDIUM | 48 hours |
| HIGH | 24 hours |
| URGENT | 8 hours |
## Ticket Categories

- Academic
- Technical
- Financial
- Administrative
- Other
## Ticket Information

Each ticket contains:

- Student
- Subject
- Description
- Category
- Priority
- Status
- Assigned Staff
- Created Date
- Updated Date
- SLA Due Date
- Resolution Date
- Resolution Notes
- Pending Reason
- Escalation Status

The system also calculates ticket age and identifies overdue tickets.
## Activity History

The system maintains activity history for important ticket actions such as:

- Ticket creation
- Status changes
- Assignment changes
- Moving a ticket to pending
- Ticket resolution

This provides a basic audit trail for ticket processing.
## User Roles

### Student
- Creates support tickets
- Provides ticket details
- Tracks ticket status

### Staff
- Views assigned tickets
- Updates ticket status
- Handles pending actions
- Adds resolution information

### Admin
- Manages users
- Manages tickets
- Assigns tickets to staff
- Monitors ticket status and activity
- Uses Django Admin for management
## Architecture

The application follows a Django-based architecture:

```text
                    Users
          Student / Staff / Admin
                       |
                       v
                Django Admin
                       |
                       v
              Django Application
                       |
        +--------------+--------------+
        |              |              |
        v              v              v
    Accounts        Tickets        Dashboard
                       |
                       v
                 SQLite Database
## Technology Used

- Python
- Django
- Django REST Framework
- SQLite
- HTML/CSS
- Git
- GitHub
## Project Structure

```text
student-support-system2/
│
├── backend/
│   ├── config/
│   ├── accounts/
│   ├── tickets/
│   ├── dashboard/
│   ├── manage.py
│   └── db.sqlite3
│
├── .gitignore
└── README.md
## How to Run

### Start the Backend

```powershell
cd backend
python manage.py runserver
## Validation and Testing

The following functionality was tested:

- Django system checks
- Database migrations
- Ticket creation
- Ticket status changes
- Ticket assignment
- Pending ticket handling
- SLA calculation
- Overdue detection
- Escalation tracking
- Ticket activity history
- Django Admin search and filtering
## Current Prototype

The current prototype is implemented primarily using Django Admin.

The core ticket management workflow includes:

- Ticket creation and management
- Priority and status management
- Staff assignment
- SLA tracking
- Ticket ageing
- Overdue detection
- Escalation tracking
- Resolution tracking
- Activity history
## Future Enhancements

- Student-facing web interface
- Staff dashboard
- REST API endpoints
- Role-based permissions
- Email/SMS notifications
- File attachments
- Ticket comments
- Advanced reporting
- SLA breach notifications
- Production deployment and monitoring
## Trade-offs

The prototype focuses on implementing the core ticket management workflow within the available development time.

Django Admin was used as the primary management interface so that the ticket lifecycle, SLA tracking, assignment, escalation, resolution, and activity history could be implemented and tested efficiently.
## AI Usage

AI tools were used during development for:

- Designing the ticket data model
- Planning the ticket workflow
- Implementing Django models
- Configuring Django Admin
- Troubleshooting migration and model errors
- Improving project documentation

AI-generated suggestions were reviewed, tested, and modified before being included in the project.