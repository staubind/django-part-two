from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User
# Create your views here.
def index(request):
    return HttpResponse('<h1>HELLO THERE, GENERAL GRIEVOUS</h1>')

def help(request):
    help_context = {"help":"this is the help variable test"}
    return render(request, 'second_app/help.html', context=help_context)

def user(request):
    user_context = {'users':User.objects.all()}
    return render(request, 'second_app/users.html', context=user_context)