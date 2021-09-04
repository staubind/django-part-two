from django.shortcuts import render # this render function renders templates
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':"Hello, II'm now coming from first_app/index.html"}
    # takes a request and the file you'd like to use, and the context variables you'd like it to have access to
    return render(request, 'first_app/index.html', context=my_dict) 