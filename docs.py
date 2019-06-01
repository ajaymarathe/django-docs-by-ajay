"""project structure"""

[projectname]/ # main project '''personal_portfolio'''
├── [projectname]/ # subfolder '''personal_portfolio'''
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── [projectname]/ # this folder is for templating the project '''projects'''
│   │   [migrations] # migrations file goes inside this folder
│   │   [static] # all asstes will goes here, like imgs, css,js
│   │   [templates]
│   │     ├──project_detail.html
│   │     ├──project_index.html
│   ├──__init__.py
│   ├──admin.py
│   ├──apps.py
│   ├──models.py
│   ├──tests.py
│   ├──urls.py
│   └── views.py
├── [templates]/
│   ├──base.html # define here your layout, so you can extends it in every file.
└── manage.py

'''how to set mysql database to django -'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'portfolio', #database name will be here
        'USER': 'root', # user name here
        'PASSWORD': '', # password here
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# manage static files

{% load static %} # first add this in top of the file
<img src="{% static "my_app/example.jpg" %}" alt="My image"> # then you will get direct access to the static directory

# create models and migrations

from django.db import models

class Project(models.Model): # create a function
    title = models.CharField(max_length=100) # then add fields
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

# handel routes in django

'''' main project'''

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("projects/", include("projects.urls")),
]

'''html templates'''

from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]

'''html templates views'''

# Create your views here.

from django.shortcuts import render
from projects.models import Project

#show all portfolio page.
def project_index(request): #define the function with request
    projects = Project.objects.all() # get all data in projects
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context) # return context as parameters to project_index.html view

# show detail portfolio
def project_detail(request, pk): #define function with request and primary key
    project = Project.objects.get(pk=pk) # here get the project data by primary key
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context) # return context as project data to the html

"""base layout file to extend in all project"""

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    {% load static %} #load static here so you can use static
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{% static "css/material.css" %}">

    <title>Hello, world!</title>
  </head>
  <body>
    # you page content will go here
    {% block page_content %}{% endblock %}

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>

'''if we create new app, then we have defined it in INSTALLED_APPS'''
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projects', #like here I have defined projects
]

'''once we create template layout file, then we have to give that path in DIRS - '''

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"], # here add templates path, so you can extends layout file direct in any file
    },
]

''' got this error - Error loading MySQLdb Module &#39;Did you install mysqlclient or MySQL-python'''

-> pip install pymysql

Then, edit the __init__.py file in your project origin dir(the same as settings.py)

import pymysql

pymysql.install_as_MySQLdb()





