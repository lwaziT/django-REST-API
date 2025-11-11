from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def students(request):
    students = [
        {
            'id': 1,
            'Name' : 'Lwazi Tobose',
            'Title' : 'Python Backend Engineer',
        }
    ]
    return HttpResponse(students)