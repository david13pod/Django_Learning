import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pro_Two.settings')

import django
django.setup()

import random

from faker import Faker
from app_two.models import User

fakegen=Faker()

def userpopulate(N=20):
    for entry in range(N):
        fakefname=fakegen.first_name()
        fakelname=fakegen.first_name()
        fakeemail=fakegen.email()

        fuser=User.objects.get_or_create(firstname=fakefname,lastname=fakelname,email=fakeemail)[0]



if __name__=='__main__':
    print('populating script')
    userpopulate(20)
    print('Population Complete')