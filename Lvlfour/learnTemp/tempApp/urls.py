from django.urls import path
from tempApp import views

app_name ='tempApp'

urlpatterns=[
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),

]