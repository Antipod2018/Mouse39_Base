from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить товар", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
def index(request):
    posts = notebook.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Mouse39',
        'cat_selected': 0,
    }
    return render(request, 'notebooks/index.html', context=context)

def show_category(request, cat_id):
    posts = notebook.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по товарам',
        'cat_selected': cat_id,
    }
    return render(request, 'notebooks/index.html', context=context)


def about(request):
    return render(request, 'notebooks/about.html', {'menu': menu , 'title': 'о приложении'})

def addpage(request):
    return HttpResponse("Добавить товар")

def contact(request):
    return HttpResponse("Добавить товар")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"отображение товара с ID = {post_id}")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Not found</h1>')

