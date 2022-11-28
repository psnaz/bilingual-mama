from django.shortcuts import render #, get_object_or_404, reverse to be added?
#from django.views import generic, View -->> CI Django Walkthrough
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
