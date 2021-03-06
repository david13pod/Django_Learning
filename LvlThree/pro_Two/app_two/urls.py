from django.urls import path
from app_two import views

urlpatterns=[
    path('',views.index2,name='index2'),
    path('users/',views.index3,name='index3'),
]