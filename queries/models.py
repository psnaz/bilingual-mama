from django.db import models
from django.contrib.auth.models import User

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
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
