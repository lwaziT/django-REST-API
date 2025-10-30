from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    campus = models.CharField(max_length=50)

    def __str__(self):
        return self.name