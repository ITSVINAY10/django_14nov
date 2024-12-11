from django.shortcuts import render
from django.http import HttpResponse

def wish2(request):
    return HttpResponse('<h1> Hello this is from second Application </h1>')



