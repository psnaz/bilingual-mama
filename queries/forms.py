from django import forms
from django.forms import ModelForm
from .models import Query

class QueryForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Query
        fields = [
            'name', 'surname', 'email', 'status',
            'subject', 'message'
        ]
