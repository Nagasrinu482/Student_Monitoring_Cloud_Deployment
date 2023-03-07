"""Student_Monitoring_Cloud_Deployment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student.views import login, logout, activateAccount, facultyregistration, studentregistration, \
    getfacultys, \
    getstudents, \
    deletefaculty, deletestudent, viewattendanceaction, addattendance, viewmarks, viewmarksaction, uploadmarks, \
    viewstudentattendance, uploadassignmentaction, viewassignments

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [

    path('admin/', admin.site.urls),

    path('',TemplateView.as_view(template_name = 'index.html'),name='login'),
    path('login/',TemplateView.as_view(template_name = 'index.html'),name='login'),
    path('loginaction/',login,name='loginaction'),
    path('activateAccount/',activateAccount,name='activateAccount'),
    path('logout/',logout,name='logout'),

    path('facultyregistration/',TemplateView.as_view(template_name = 'facultyregistration.html'),name='registration'),
    path('facultyregaction/',facultyregistration,name='regaction'),

    path('studentregistration/',TemplateView.as_view(template_name = 'studentregistration.html'),name='registration'),
    path('studentregaction/',studentregistration,name='regaction'),

    path('getstudents/',getstudents,name='regaction'),
    path('getfacultys/',getfacultys,name='regaction'),

    path('deletestudent/',deletestudent,name='regaction'),
    path('deletefaculty/',deletefaculty,name='regaction'),

    path('addattendance/',TemplateView.as_view(template_name = 'addattendance.html'),name='registration'),
    path('addattendanceaction/',addattendance, name='regaction'),

    path('viewattendance/',viewattendanceaction,name='regaction'),
    path('viewstudentattendance/', viewstudentattendance, name='regaction'),

    path('uploadmarks/',TemplateView.as_view(template_name = 'uploadmarks.html'), name='registration'),
    path('uploadmarksaction/',uploadmarks, name='registration'),
    path('viewmarks/',viewmarks, name='registration'),
    path('viewmarksaction/',viewmarksaction, name='regaction'),

    path('uploadassignment/',TemplateView.as_view(template_name = 'uploadassignment.html'), name='registration'),
    path('uploadassignmentaction/',uploadassignmentaction, name='registration'),
    path('viewassignments/',viewassignments, name='regaction'),
]
