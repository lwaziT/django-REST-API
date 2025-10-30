from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

# Create your views here.
def studentsView(request):
    students = Student.objects.all()
    return JsonResponse(students)
