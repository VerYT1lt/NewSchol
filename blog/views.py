from django.shortcuts import render
import datetime

def your(request):
    now=datetime.datetime.now()
    print("Date: "+ now.strftime("%Y-%m-%d"))
# Create your views here.
