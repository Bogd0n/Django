from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def about(request):
    return HttpResponse("Это страница О нас!")

def contact(request):
    return HttpResponse("Контакты: email@example.com, +7 123 456 7890")
