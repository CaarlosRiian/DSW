from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("<h1>Hello, World!</h1> <p>mudei</p>")

