# Django REST API
## Overview
This follows a demo tutorial on API development using the django rest framework. The
tutorial explores funtion-based view vs class-based views, implementing serializers, 
handling CRUD operations via: Mixins, Generics and Viewsets. It also covers pagination, filtering
and ordering.The project includes multiple Django apps (students, employees, blogs, etc.) and exposes clean CRUD endpoints following REST best practices.

## Tech Stack
- Python (Django)

## Project structure
django-REST-API/
│
├── api/                     # common API logic (if present)
├── students/                # Django app for student-related models & API
├── employees/               # Django app for employee-related models & API
├── blogs/                   # Django app for blog-related models & API
├── django_rest_main/        # main Django project settings & config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py (if present)
├── manage.py
├── db.sqlite3               # SQLite database (for development / demo)
├── README.md                # This file
└── other project files / env info

## Future improvements
- Add unit tests for models, serializers, and views
