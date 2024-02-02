"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.user_login,name='user_login'),
    path('login/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('computer',views.computer,name='computer'),
    path('com1',views.com1,name='com1'),
    path('com2',views.com2,name='com2'),
    path('com3',views.com3,name='com3'),
    path('com4',views.com4,name='com4'),
    path('com5',views.com5,name='com5'),
    path('com6',views.com6,name='com6'),
    path('com7',views.com7,name='com7'),
    path('com8',views.com8,name='com8'),
    path('maths',views.maths,name='maths'),
    path('mat1',views.mat1,name='mat1'),
    path('mat2',views.mat2,name='mat2'),
    path('mat3',views.mat3,name='mat3'),
    path('mat4',views.mat4,name='mat4'),
    path('mat5',views.mat5,name='mat5'),
    path('mat6',views.mat6,name='mat6'),
    path('mat7',views.mat7,name='mat7'),
    path('mat8',views.mat8,name='mat8'),
    path('english',views.english,name='english'),
    path('eng1',views.eng1,name='eng1'),
    path('eng2',views.eng2,name='eng2'),
    path('eng3',views.eng3,name='eng3'),
    path('eng4',views.eng4,name='eng4'),
    path('eng5',views.eng5,name='eng5'),
    path('eng6',views.eng6,name='eng6'),
    path('eng7',views.eng7,name='eng7'),
    path('eng8',views.eng8,name='eng8'),
    

]
