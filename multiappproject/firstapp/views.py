from django.shortcuts import render
from django.http import HttpResponse 

def wish1(request):
    return HttpResponse('<h1> Hello this is from first Application </h1>')

