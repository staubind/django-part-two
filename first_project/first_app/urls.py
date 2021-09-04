from django.conf.urls import url
from django.urls.resolvers import URLPattern
from django.urls import path

# our stuff
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
]