from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'professor/index.html')
def register(request):
    return render(request, 'professor/register.html')
def login(request):
    return render(request, 'professor/login.html')