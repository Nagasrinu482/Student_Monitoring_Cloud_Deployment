from django.contrib import admin

# Register your models here.
from student.models import FacultyModel, StudentModel, AttendanceModel, MarksModel

admin.site.register(FacultyModel)
admin.site.register(StudentModel)
admin.site.register(AttendanceModel)
admin.site.register(MarksModel)