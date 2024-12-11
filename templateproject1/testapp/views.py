from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date = datetime.datetime.now()
    msg = 'Hello Guest Very Good'
    h = int(date.strftime('%H'))
    if h < 12:
        msg += 'Morning'
    elif h < 16:
        msg += 'Afternoon'  
    elif h < 21:
        msg += 'Evening'        
    else:
        msg += 'Night'
    my_dict = {'insert_date':date,'insert_msg':msg}   
    return render (request,'testapp/wish.html',my_dict)
