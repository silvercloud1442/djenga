from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "about site", "url_name": "about"},
        {'title': "add page", "url_name": "add_page"},
        {'title': "Contact page", "url_name": "contact"},
        {'title': "Login", "url_name": "login"}
]

def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected' : 0,
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def addpage(request):
    return HttpResponse('Add page')

def contact(request):
    return HttpResponse('Contact page')

def login(requsest):
    return HttpResponse('Authorization')

def show_post(request, post_id):
    return HttpResponse(f"Post id --------- {post_id}")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Categorys',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)