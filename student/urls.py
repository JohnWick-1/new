"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from app import views
from app import tests

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/',include('app.urls')),
    path('stud2/',views.Student2View.as_view()),
    url(r'^$', schema_view),
    path('test/',views.test1),
    path('gtok/', views.token),
    path('token/',views.get_token),
    # path('test/',tests.test_stu1_db),
    path('login/',views.user_login),
    path('logout/',views.user_logout)

    # print('inside project urls')
]

print('inside project urls')
