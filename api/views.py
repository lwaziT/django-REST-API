from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from students.models import Student

# Create your views here.
@api_view(['GET'])
def studentsView(request):

    if request.method == 'GET':
        # Get all the data from the student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

