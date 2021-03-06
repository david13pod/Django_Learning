from django.shortcuts import render
from FormApp import forms

# Create your views here.

def index(request):
    return render(request,'FormApp/index.html')


def form_name_view(request):
    form=forms.Formname()

    if request.method =='POST' :
        form=forms.Formname(request.POST)

        if form.is_valid():

            print ("Validation Successful")
            print("Name:"+form.cleaned_data['name'])
            print("Email:"+form.cleaned_data['email'])
            print("Text:"+form.cleaned_data['text'])


    return render(request,'FormApp/form_page.html', {'form':form})