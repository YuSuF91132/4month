from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Это моя первая главная страница которая была создана на Django</h4>")

def about(request):
    about_us = "Этот сайт был создан с помощью Django"
    return HttpResponse(f"<h4>О нас</h4>{about_us}")

def contact(request):
    contact1 = "Номер телефона:+12341234"
    return HttpResponse(f"<h4>Наши Контакты</h4>{contact1}")

def help(request):
    return HttpResponse("<h4>Чем мы можем помочь?</h4>")  