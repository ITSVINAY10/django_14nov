from django.shortcuts import render
import datetime,random
# Create your views here.
def result_view(request):
    msg_list = [
        'The golden days ahead',
        'Better to sleep more time even in classroom',
        'Tomorrow will be the best day of your life',
        'Tomorrow is the perfect day to propose ur GF',
        'Very soon you will get a job',
    ]
    names_list = ['Vinay','Vijay','Manikanta','Rajesh','Raghu','Varun','Lakshman']
    name_list = ['Ramya','Mallika','Keerthi','Vishnu','Deepika','Swarupa']
    time = datetime.datetime.now()
    h = int(time.strftime('%H'))
    if h < 12:
        s = 'Good Morning'
    elif h < 16:
        s = 'Good Afternoon'
    elif h < 21:
        s = 'Good Evening'
    else:
        s = 'Good Night'    
    name = random.choice(name_list)
    names = random.choice(names_list)
    msg = random.choice(msg_list)
    my_dict = {'time':time,'names':names,'name':name,'msg':msg,'wish':s}
    return render(request,'testapp/astrology.html',my_dict)