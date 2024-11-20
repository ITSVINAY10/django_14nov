from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def exams_view(request):
    return HttpResponse('<h1>Exams view</h1>')
def fees_view(request):
    return HttpResponse('<h1>Fees view</h1>')
def attendance_view(request):
    return HttpResponse('<h1>Attendance view</h1>')