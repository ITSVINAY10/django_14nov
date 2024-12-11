from django.shortcuts import render
import datetime
# Create your views here.
def info_view(request):
    date = datetime.datetime.now()
    name = 'Django'
    prerequisite = 'Python'
    my_dict = {'time':date,'name':name,'prerequisite':prerequisite}
    return render(request,'testapp/results.html',my_dict)
