"""
This is my original custom model with associated functionalities that 
hasn't been used in the CI Django Walkthrough projects. It has been 
created by following and tweaking the Youtube Django Tutorial #9: 
A More Complex Form (2022) by Django tutorials (see README file) 
AND with a kind advice and help of my mentor.
"""

from django import forms
from django.forms import ModelForm
from .models import Query, STATUS_CHOICES


class QueryForm(forms.ModelForm):
    required_css_class = 'required'

    status = forms.CharField(
        label="Status",
        widget=forms.Select(choices=STATUS_CHOICES,
                            attrs={'class': 'form-control', 'id': 'status'}),
    )
    
    class Meta:
        model = Query
        fields = [
            'name', 'surname', 'email', 'status',
            'subject', 'message'
        ]
