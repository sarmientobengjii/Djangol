from django.shortcuts import render
from django.http import HttpResponse

#views here

def index(request):
    return HttpResponse("Hello, Voters. You're at the polls page.")

def user(request):
    return HttpResponse("USER here")

def voter(request):
    return HttpResponse("Voters here")