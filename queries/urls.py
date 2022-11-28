# not sure this is any good at all
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='queries'),
    path('query_form', views.query_form, name='query_form'),
    path('query_submitted', views.query_submitted, name='query_submitted')
]
