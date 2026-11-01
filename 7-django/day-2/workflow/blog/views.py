from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotAllowed


# Create your views here.
def home(request):
    return HttpResponse("Hello Django Blog!")
