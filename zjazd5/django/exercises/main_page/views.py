from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main_page(request):
    return HttpResponse(content="To jest main page")

def hello_world(request):
    return HttpResponse(content="Hello world")

def hello_personalized(request,name):
    return HttpResponse(content=f"Hello world {name}")




