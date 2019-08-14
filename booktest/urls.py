from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path

import booktest
from booktest import views
from booktest.views import *

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('index1', views.index1,name='index1'),
    path('index2', views.index2),
    path('index3', views.index3),

    path('index5', views.index5),
    re_path('^detail-(\d+)$', views.detail),
    path('detail_get', views.detail_get),
    path('detail_response', views.detail_response),
    #url('(\d+)', views.show,name='show'),
]
