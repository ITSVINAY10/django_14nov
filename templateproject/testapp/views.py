from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date = datetime.datetime.now()
    return render(request,'testapp/wish.html',{'insert_date':date})