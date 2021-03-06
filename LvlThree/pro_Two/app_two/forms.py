from django import forms
from django.forms import fields
from app_two.models import User

class Newuserform(forms.ModelForm):
    class Meta():
        model=User
        fields='__all__'