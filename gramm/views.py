from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Instagram')
