#-*- coding: utf-8 -*-
""" 자보 리스트 보여주기 기능 구현 """
from models import Article, Poster
from django.http import HttpResponse
from django.shortcuts import render
import os


# Create your views here.

def view(request, page=1):
    """
        자보 리스트를 보여준다.
        request : http request
        page : page number
    """
    if request.method == 'POST':
        pass
    no_of_articles = Article.objects.count()
    articles = Article.objects.all().order_by('-written_datetime')
        #need to make it more efficient
    per_page = 4
    page = int(page)
    chosen_articles = articles[(page-1)*per_page : page*per_page]
    chosen = []
    for each in chosen_articles:
        chosen.append(each.poster.all()[0].picture.url)
    print len(chosen)
    #other_pages = filter(lambda x: x > 0, range(int(page)-3, int(page)+4))
    #other_pages = filter(lambda x: x < ((no_of_articles/4)+2), other_pages)
    print no_of_articles
    if page < 5:
        if page+3 > (no_of_articles/4):
            other_pages = range(1, 2+(no_of_articles-1)/4)
        else: other_pages = range(1, page+4)
    else:
        if page+3 > (no_of_articles/4):
            other_pages = range(page-3, 2+(no_of_articles-1)/4)
        else: other_pages = range(page-3, page+4)
    # what if the page number overflows?
    #if page>(1+(no_of_articles-1)/4):
    print other_pages
    ctx = {'chosen':chosen,
            'page':page,
            'other_pages':other_pages,
            'no_of_articles':no_of_articles}
    return render(request, 'board/view.html', ctx)
