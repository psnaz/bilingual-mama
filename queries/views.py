#from django.shortcuts import render, get_object_or_404, reverse
#from django.views import generic, View
#from django.http import HttpResponseRedirect
#from .models import Query
#from .forms import QueryForm

#def query_req(request):
    #submitted = False
   # if request.method == 'POST':
        #form = QueryForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return HttpResponseRedirect('/query/?submitted=True')
    #else:
        #form = QueryForm()
        #if 'submitted' in request.GET:
            #submitted = True

    #return render(request, 'queries/query.html')
