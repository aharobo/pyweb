from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

from django.db.models import Max

from django.http import *

from booktest.models import *

from datetime import datetime


def index5(request):
    return HttpResponse('Test')

def detail(request,p1):
    return HttpResponse('Test:'+p1)

def detail_get(request):
    return JsonResponse(request.GET)
    #return HttpResponse('Test:'+ request.GET)

def detail_response(request):

    response=HttpResponse()
    v = request.COOKIES.get('h1')
    if v!=None:
        response.write('<h1>'+request.COOKIES['h1']+'</h1>')
    else:

        response.set_cookie('h1','AHA , SEE YOU AGAIN',None,datetime(2019,9,8))
        response.write('inited.')

    return  response;


def index(request):

    r = HttpResponse()
    c='<meta name="viewport" content="width=device-width, initial-scale=1.0,maximum-scale=1.0, user-scalable=no"/>'
    c=c+"我是视图222444"
    r.write(c)
    r.flush()
    return  r


def index1(request):

    list=BookInfo.books1.filter(heroinfo__hcontent__contains='八')
    return render(request, 'booktest/index1.html', {'list':list})


def index2(request):
    list=HeroInfo.m.filter(hcontent__contains='七')
    return render(request, 'booktest/index2.html', {'list':list})

def index3(request):

    r=HeroInfo.m.aggregate(Max('hgender'))

    return HttpResponse('Test:', str(r))

def show(request,id):
    book=BookInfo.books1.get(pk=id)
    herolist=book.heroinfo_set.all()
    context={'list':herolist}
    return render(request,'booktest/show.html',context)