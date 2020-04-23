from django.shortcuts import render
from django.http import HttpResponse  #needed to allow browser to return view

# Create your views here.
def myView(requests):  #creates the page/view for "Hello"
    return HttpResponse("Welcome to Anthony's Site!") #returns what we want to be displayed on the site/page