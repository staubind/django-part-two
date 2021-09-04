from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>HELLO THERE, GENERAL GRIEVOUS</h1>')

def help(request):
    help_context = {"help":"this is the help variable test"}
    return render(request, 'second_app/help.html', context=help_context)