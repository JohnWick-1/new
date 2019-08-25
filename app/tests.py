from django.test import TestCase
# from .models import Student2,Student
# Create your tests here.

'''
def test_stu1_db(request):
    print('inside test_stu1_db')
    

    if request.method == 'POST':
        print(request.data)
        print('****** POST *****',request.POST["first_name"])
        stud = Student2(first_name=request.data.get('first_name'),
                        last_name=request.data.get('last_name'),
                marks=request.data.get('marks'),DOB=request.data.get('DOB'))

        stud.save(using='replica')
        stud.save(using='default')
        print("%%%%%%%%%% data save %%%%%%%%%%")

        print(stud)

    else:
        obj = Student2.objects.using('replica').all()
        print(obj)
'''

'''
from rest_framework.authtoken.models import Token   #for token
from django.contrib.auth.models import User  

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

'''
'''
@csrf_exempt
def get_token(request):
    print('inside det token')
    print(request.method)
    print(request.POST)
    # print('Username is -- ',request.POST['username'])
    #userin = User.objects.get(username=req.POST['username'])
    #token = Token.objects.create(user=userin)
    # u = User.objects.get(username=request.POST['admin'])
    u = User.objects.get(username='admin')
    key = Token.objects.get(user_id=u.id)
    print(key)
    return HttpResponse(key)

#
# import requests
#
# data= requests.get('https://www.accuweather.com/en/in/pune/204848/weather-forecast/204848')
'''



