from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

menu = [{'title': "about site", "url_name": "about"},
        {'title': "add page", "url_name": "add_page"},
        {'title': "Contact page", "url_name": "contact"},
        {'title': "Login", "url_name": "login"}
]

def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
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
    post = get_object_or_404(Women, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, "women/post.html", context=context)

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Categorys',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)