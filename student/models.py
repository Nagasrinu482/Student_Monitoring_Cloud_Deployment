from django.db import models

from django.db.models import Model

class FacultyModel(Model):

    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    department=models.CharField(max_length=50)

class StudentModel(Model):

    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    status=models.CharField(max_length=50)

class AttendanceModel(Model):

    username=models.CharField(max_length=50,default="")
    date = models.CharField(max_length=50,default="")
    isattended=models.CharField(max_length=50,default="")


class MarksModel(Model):
    username=models.CharField(max_length=50,default="")
    subjectcode = models.CharField(max_length=50,default="")
    marks=models.CharField(max_length=50,default="")

class AssignmentModel(Model):
    document=models.FileField(upload_to="documents")
    subjectcode = models.CharField(max_length=50,default="")
    department = models.CharField(max_length=50)