from django.shortcuts import render
from django.http import HttpResponse

#views here

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def user(request):
    return HttpResponse("USER here")