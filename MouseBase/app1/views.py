from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import *

menu = ["О приложении mouse39", "добавить товар", "login", "Сообщить об ошибке"]
def index(request):
    posts = notebook.objects.all()
    return render(request, 'notebooks/index.html', {'posts': posts, 'menu': menu, 'title': 'главная страница'})

def about(request):
    return render(request, 'notebooks/about.html', {'menu': menu , 'title': 'о приложении'})

def categories(request, catid):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Страница с ноутами</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('/')
    return HttpResponse(f"<h1>Архив ноутов по датам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Not found</h1>')
