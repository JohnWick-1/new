from django.shortcuts import render
from .serializers import Student2Serializer
from django.http import HttpResponse
import json

from rest_framework.views import APIView
from .serializers import StudentSerializer
from .models import Student,Student2
# Create your views here.
from rest_framework.decorators import action

from rest_framework.viewsets import ModelViewSet


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


from rest_framework.decorators import list_route
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework import status
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


class StudentViewSet(ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]


    serializer_class = StudentSerializer
    queryset = Student.objs.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        obj = Student(first_name=request.POST['first_name'],last_name=request.POST['last_name'],
                       marks=request.POST['marks'],DOB=request.POST['DOB'])
        obj.objs.using('replica').save()
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    @action(methods=['POST'],detail=True)
    @list_route(renderer_classes=[StaticHTMLRenderer])
    def own_delete_method(self, request, *args, **kwargs):
        # id =request.GET['id']
        # stud = Student2.objects.get(id=id)
        # stud.delete()
        return HttpResponse('ggjgfgjd')


class Student2View(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    @login_required(login_url='/login')
    def get(self, request, format=None):

        s=Student2.objects.using('replica').all()
        serializer = Student2Serializer(s,many=True)
        print(serializer)
        # from django.http import HttpResponse
        return Response(serializer.data)

    @login_required(login_url='/login')
    def post(self,request):
        stud = Student2(first_name=request.data.get('first_name'),last_name=request.data.get('last_name'),
                        marks=request.data.get('marks'),DOB=request.data.get('DOB'))
        print('*'*100)
        stud.save(using='replica')
        stud.save(using='default')
        print('*'*100)
        s=Student2.objects.all()
        serializer = Student2Serializer(s,many=True)
        msg='data save'
        return render(request,'app/home.html',context={'msg':msg})



@login_required(login_url='/login')
def test1(request):

    print('*'*100)
    return HttpResponse(User.objects.all())



from rest_framework.authtoken.models import Token   #for token
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def get_token(request):

    user = User.objects.get(username=request.POST['username'])
    key = Token.objects.get(user_id=user.id)
    print(key)
    return HttpResponse(key)


def user_login(request):
    print(request.body)
    print(request.session)
    if request.method=='POST':
        print('inside post')
        username = request.POST['name']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user:
            print('inside user')
            login(request,user)
            request.session['name'] = username
            request.session['password'] = password
            msg = str(user)+' ' + 'log in'
            return render(request,'app/home.html',context={'msg':msg})
        else:
            msg = 'invalid data'
            return render(request, 'app/login.html',context={'msg':msg})
    else:
        return render(request,'app/login.html')


@login_required(login_url='/login')
def user_logout(request):
    if request.method=='POST':
        del request.session['name']
        del request.session['password']
        logout(request)
        msg = 'successfully logout '
        return render(request, 'app/login.html', context={'msg': msg})
    return HttpResponseRedirect(reverse('user_login'))


def token(request):

    return render(request,'app/token.html')


def set_cookies(request):
    name=request.POST['name']
    msg = request.POST['msg']

    pass

def get_cookies(request):
    pass