from django.shortcuts import render # this render function renders templates
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    # my_dict = {'insert_me':"Hello, II'm now coming from first_app/index.html"}
    # takes a request and the file you'd like to use, and the context variables you'd like it to have access to
    return render(request, 'first_app/index.html', context=date_dict) 