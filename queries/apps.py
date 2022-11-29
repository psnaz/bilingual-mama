"""
This is my original custom model with associated functionalities that 
hasn't been used in the CI Django Walkthrough projects. It has been 
created by following the Youtube Django Tutorial #9: A More Complex Form (2022) 
by Django tutorials (see README file)
"""

from django.apps import AppConfig


class QueriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'queries'
