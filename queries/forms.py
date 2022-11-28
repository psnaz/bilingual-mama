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
