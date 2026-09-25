# Student Support & Ticket Management System

## Overview

A Django-based student support and ticket management system designed to help students raise support requests and allow staff/admin users to manage, prioritize, assign, and track tickets.

## Features

- User profiles with Student, Staff, and Admin roles
- Create and manage support tickets
- Ticket categories
- Priority management
- Ticket status tracking
- Ticket assignment to staff
- Pending ticket handling
- Escalation tracking
- SLA-related fields
- Resolution notes
- Resolution timestamp
- Django Admin interface

## Ticket Workflow

Open → In Progress → Pending → Resolved → Closed

## Technology Stack

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
│   ├── accounts/
│   ├── tickets/
│   ├── dashboard/
│   ├── config/
│   └── manage.py
│
├── venv/
└── .gitignore