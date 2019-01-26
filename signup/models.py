from django.db import models

# Create your models here.
class Student(models.Model):
    student_fname = models.CharField(max_length=100)
    student_lname = models.CharField(max_length=100)
    student_email = models.CharField(max_length=50)
    student_username = models.CharField(max_length=100)
    student_password = models.CharField(max_length=20)
    student_date = models.DateField()



