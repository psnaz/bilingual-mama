"""
This is my original custom model with associated functionalities that 
hasn't been used in the CI Django Walkthrough projects. It has been 
created by following and tweaking the Youtube Django Tutorial #9: 
A More Complex Form (2022) by Django tutorials (see README file) 
AND with a kind advice and help of my mentor.
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='queries'),
    path('query_form', views.query_form, name='query_form'),
    path('query_submitted', views.query_submitted, name='query_submitted')
]
