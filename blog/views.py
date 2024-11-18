from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная')

def accounts(request, name='NoName', age=0):
    return HttpResponse(f'Имя: {name}, Возраст: {age}')

# def your(request):
#     now=datetime.datetime.now()
#     print("Date: "+ now.strftime("%Y-%m-%d"))
def catalog():
    return HttpResponse('Oiniajs')


def contact():
    return HttpResponse('assmmxasjasjkxm')