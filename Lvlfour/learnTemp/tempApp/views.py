from django.shortcuts import render

# Create your views here.
def index(request):
    contextdict={'text':'Hello Everyone','number':1000 }
    return render(request,'tempApp/index.html' , contextdict)

def other(request):
    return render(request,'tempApp/other.html')


def relative(request):
    return render(request,'tempApp/relative_url_temp.html')
