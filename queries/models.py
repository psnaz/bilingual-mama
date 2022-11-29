from django.db import models
from django.contrib.auth.models import User

"""
This is my original custom model with associated functionalities that 
hasn't been used in the CI Django Walkthrough projects. It has been 
created by following the Youtube Django Tutorial #9: A More Complex Form (2022) 
by Django tutorials (see README file)
"""

STATUS_CHOICES = (
    ('PARENT', 'I am a parent'),
    ('EXPECTING', 'I am or we are expecting a baby'),
    ('BLOGGER', 'I am a blogger'),
    ('OTHER', 'I am just someone who wants to get in touch'),
)

class Query(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    subject = models.TextField(max_length=50)
    message = models.TextField()
    submitted = models.DateField(auto_now_add=True)
    answerdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.id)
