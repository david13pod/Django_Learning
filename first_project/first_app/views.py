
from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Webpage,Topic

# Create your views here.

# def index(request):
#     return HttpResponse("Hello world")

def index(request):
    webpage_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpage_list}
    return render(request,'first_app/indexa.html',context=date_dict)

def index2(request):
    mydict={'insert_me':"I am from frist_app/index"}
    return render(request,'first_app/index.html',context=mydict)