from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello World. This is my Elastic Insurance Project')