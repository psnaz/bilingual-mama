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
