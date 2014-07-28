#-*- coding: utf-8 -*-
""" 자보 리스트 보여주기 기능 구현 """
from models import Article, Poster
from django.http import HttpResponse
from django.shortcuts import render
import os


# Create your views here.

def view(request):
    """
        자보 리스트를 보여준다.
        request : http request
        page : page number
    """
    if request.method == 'POST':
        pass
    no_of_articles = Article.objects.count()
    articles = Article.objects.all().order_by('id')

    template = 'board/view.html'
    page_template = 'board/view_page.html'
    ctx = {'chosen':articles,
            'no_of_articles':no_of_articles,
            'page_template':page_template,
            }
    if request.is_ajax():
        template = page_template

    return render(request, template, ctx)
