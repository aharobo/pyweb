from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from booktest.models import ContactInfo


def index(request):

    contact_list=ContactInfo.objects.all();
    context={'list':contact_list}

    response=HttpResponse()
    v = request.COOKIES.get('h1')
    if v!=None:
        response.write('<h1>'+request.COOKIES['h1']+'</h1>')
    else:

        response.set_cookie('h1','AHA , SEE YOU AGAIN',None,datetime(2019,9,8))
        response.write('inited.')

    return  response;

    #return redirect('/book')
    #return render(request,'web/index.html',context)