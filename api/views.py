from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer
from .paginations import CustomPagination
from employees.filters import EmployeeFilter

import employees
from blogs.models import Blog
from .serializers import StudentSerializer, EmployeesSerializer
from students.models import Student
from employees.models import Employee
from rest_framework import mixins, generics

# Create your views here.

# Function-based views
@api_view(['GET', 'POST'])
def studentsView(request):

    if request.method == 'GET':
        # Get all the data from the student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # Send data to the student table
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):

    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # Get student data by id
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # Update student data
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete student data
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return None

# Class-based views
# class Employees(APIView):
#     # Get all employee objects/data
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeesSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     # Add new employee
#     def post(self, request):
#         serializer = EmployeesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class EmployeeDetail(APIView):
#     # Class to handle employee data
#
#     # Make sure employee object exists
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
#
#     # Get employee by id
#     def get(self,request,pk):
#         employee = self.get_object(pk)
#         serializer = EmployeesSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     # Update employee
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeesSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # Delete employee
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Mixins
# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeesSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)

# Mixins
# class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeesSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk)

# Generics
# class Employees (generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeesSerializer
#
# Generics
# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeesSerializer
#     lookup_field = 'pk'

# viewsets.ViewSet
# class EmployeeViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer = EmployeesSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def create(self, request):
#         serializer = EmployeesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeesSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def update(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeesSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Gives access to CRUD operations using viewsets.ModelViewSet
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
    pagination_class = CustomPagination
    filterset_class = EmployeeFilter

# Give access to CRUD operations using generics
class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
