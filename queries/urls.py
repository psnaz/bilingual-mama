from django.urls import path

from . import views

urlpatterns = [
    path('', views.query_req('queries/query.html'), name='query'),
]
