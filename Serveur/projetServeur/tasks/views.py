from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Register_view(request):
    return HttpResponse("Page d'inscription")

def Login_view(request):
    return HttpResponse("Page de connexion")