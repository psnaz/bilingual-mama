"""
This is my original custom model with associated functionalities that 
hasn't been used in the CI Django Walkthrough projects. It has been 
created by following and tweaking the Youtube Django Tutorial #9: 
A More Complex Form (2022) by Django tutorials (see README file) 
AND with a kind advice and help of my mentor.
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from .models import Query
from .forms import QueryForm


def index(request):
    template = 'queries/query.html'

    query_form = QueryForm()

    context = {
        'query_form': query_form
    }

    return render(request, template, context)


def query_form(request):
    form = QueryForm(request.POST)
    # https://docs.python.org/3/library/pdb.html
    # import pdb;pdb.set_trace()
    if form.is_valid():
        form.save()
        return redirect('query_submitted')

    return HttpResponse('Something wrong happened')


def query_submitted(request):
    return render(request, 'queries/index.html')
