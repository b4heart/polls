from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

from datetime import datetime


def index(request):
    now = datetime.now()
    current_time = now.strftime("%m-%d-%Y, %H:%M:%S")
    return HttpResponse("Hello, world. The time is: "+str(current_time))
