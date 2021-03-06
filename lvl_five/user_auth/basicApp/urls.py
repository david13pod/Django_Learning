from django.urls import path
from basicApp import views

app_name='basicApp'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]