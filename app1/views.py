from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def fun_str(request):
    return HttpResponse ("Returning as string")