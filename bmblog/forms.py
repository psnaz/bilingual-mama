from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for posting comments
    """
    class Meta:
        model = Comment
        fields = ('body',)
