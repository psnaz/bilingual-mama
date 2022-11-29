"""
This is a part of my original custom model with associated functionalities that 
hasn't been used in the CI Django Walkthrough projects. It has been 
created by following the Youtube Django Tutorial #9: A More Complex Form (2022) 
by Django tutorials (see README file)
"""
from django.contrib import admin
from .models import Query


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'surname', 'submitted', 'answerdate')
    list_filter = ('submitted', 'answerdate')
    readonly_fields = ('id', 'submitted')
    fieldsets = (
        (None, {
            'fields': ('name', 'surname', 'email', 'subject')
        }),
        ('Message Info', {
            'classes': ('collapse',),
            'fields': ('message', 'status', 'submitted')
        }),
        ('Query Admin', {
            'classes': ('collapse',),
            'fields': ('answerdate', 'username')
        }),
    )
