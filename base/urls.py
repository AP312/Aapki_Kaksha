"""aapki_kaksha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('login_page',views.login_page,name='login_page'),
    path('tic_tac_toe',views.tic_tac_toe,name='tic_tac_toe'),
    path('meditation',views.meditation,name='meditation'),
    path('memory_card',views.memory_card,name='memory_card'),
    path('draw',views.draw,name='draw'),
    path('basic_math',views.basic_math,name='basic_math'),
    path('read_news',views.read_news,name='read_news'),
]
