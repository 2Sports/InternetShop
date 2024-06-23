from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<h1>HI! This is a internet shop!</h1> <img src='https://s2.best-wallpaper.net/wallpaper/2560x1600/1907/Many-packs-of-US-dollars-money-currency_2560x1600.jpg'>")