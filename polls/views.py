from django.shortcuts import render

#views here
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Justin, bebe ni Farrah.")

