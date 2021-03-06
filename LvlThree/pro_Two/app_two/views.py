from django.shortcuts import render
from django.http import HttpResponse
# from app_two.models import User
from app_two.forms import Newuserform

# Create your views here.

def indextwo(request):
    return HttpResponse('<em>My Second App</em>')

def index2(request):
    dict2={ 'insertHere':'This is the App Home page'}
    return render(request,'secondapp/index.html',context=dict2)

def index3(request):
    form=Newuserform()

    if request.method == 'POST':
        form=Newuserform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index2(request)
        else:
            print('Error in user input')
    
    return render(request,'secondapp/user.html',{'form':form})