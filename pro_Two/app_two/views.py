from django.shortcuts import render
from django.http import HttpResponse
from app_two.models import User

# Create your views here.

def indextwo(request):
    return HttpResponse('<em>My Second App</em>')

def index2(request):
    dict2={ 'insertHere':'This is the App Home page'}
    return render(request,'secondapp/help.html',context=dict2)

def index3(request):
    user_list=User.objects.order_by('firstname')
    dict3={ 'user_records' : user_list}
    return render(request,'secondapp/user.html',context=dict3)