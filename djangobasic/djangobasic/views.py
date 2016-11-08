'''
Created on 05-Nov-2016

@author: lakshman
'''

import datetime
from django.template.loader import get_template

from django.http import Http404, HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("hello django basic user")

def tine(request):
    now = datetime.datetime.now()
    return render(request, 'current_time.html', {'current_date': now})

def hours_head(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request,'hours_head.html', {'offset':offset,'dt': dt})