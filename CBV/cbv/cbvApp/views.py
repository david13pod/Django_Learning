from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView,ListView,DetailView, CreateView,UpdateView,DeleteView
from . import models

# Create your views here.

#normal view
# def index(request):
#     return render(request,'cbvApp/index.html')

#ClassbasedView
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("From class based view")

# Template View
class IndexView(TemplateView):
    template_name='cbvApp/index.html'

#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         context['injectme']='Basic Injection'
#         return context

class SchoolListView(ListView):
    context_object_name='schools'
    model=models.School
    #gives school_list

class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model= models.School
    #returns school
    template_name='cbvApp/school_detail.html'

class SchoolCreateView(CreateView):
    fields=('name','principal', 'location')
    model=models.School

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=models.School

class SchoolDeleteView(DeleteView):
    model=models.School
    success_url=reverse_lazy("cbvApp:list")