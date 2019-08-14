from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

import web
from web import views

urlpatterns = [
    path('', views.index,name='index'),
]
