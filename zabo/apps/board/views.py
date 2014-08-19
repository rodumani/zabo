#-*- coding: utf-8 -*-
""" 자보 리스트 보여주기 기능 구현 """
from models import Article, Poster
from django.http import HttpResponse
from django.shortcuts import redirect, render
from zabo.apps.account.models import UserProfile
from django.core.serializers.json import DjangoJSONEncoder
import os
import json

# Create your views here.

MAX_HEIGHT = 240
PAGE_WIDTH = 1024
MAX_WIDTH = PAGE_WIDTH * 0.9 # For good look
def determine_space(N, length):
    remaining_width = int(PAGE_WIDTH - length) - 1
    space_n = 3 * N - 1
    space_width = remaining_width / space_n
    space_interval = [space_width] * (space_n - (remaining_width % space_n)) 
    space_interval += [space_width + 1] * (remaining_width % space_n)
    space_interval += [0]
    return space_interval

def view(request):
    """
        자보 리스트를 보여준다.
        request : http request
        page : page number
    """
    articles = Article.objects.all().order_by('?')
    template = 'board/view.html'
    page_template = 'board/view_page.html'
    if request.is_ajax():
        template = page_template

    return render(request, template, get_ctx(articles))

def category(request, category_num):
    """
        request : http request
        page : page number
    """
    category = int(category_num)
    articles = Article.objects.filter(category=category)
    template = 'board/view.html'
    page_template = 'board/view_page.html'
    if request.is_ajax():
        template = page_template

    return render(request, template, get_ctx(articles))

def search(request):
    query = request.GET.get('query', '')
    club = UserProfile.objects.filter(club_name_en=query)
    if not club:
        #TODO show search result
        return redirect('/')
    return redirect('/club/'+query)

def get_ctx(articles):
    """
        return context in redirect
        articles : want to show articles
    """

    all = []
    l = []
    length = 0
    for article in articles:
        picture = article.main_poster.picture
        new_width = MAX_HEIGHT * picture.width / picture.height
        if length + new_width > MAX_WIDTH:
            space = determine_space(len(l), length)
            line = []
            for i in range(len(l)): # determine the margin-left/right
                line.append([l[i][0], space[i*3]-1, space[i*3+1]-1, space[i*3+2]-1, l[i][1]])
            all.append(line)
            l = []
            length = 0
        l.append((picture.url, article.id))
        length += new_width

    if length != 0:
        line = []
        if length + 30*len(l) <= PAGE_WIDTH:
            for i in range(len(l)):
                line.append([l[i][0], 10, 10, 10, l[i][1]])
        else:
            for i in range(len(l)):
                line.append([l[i][0], 5, 5, 5, l[i][1]])
        all.append(line)

    page_template = 'board/view_page.html'
    ctx = {'chosen':all,
            'page_template':page_template,
            'picture_height':MAX_HEIGHT,
            }
    return ctx

def get_detail(request):
    article_id = request.GET['article_id']
    
    if not Article.objects.filter(id=article_id).exists():
        raise ValidationError("no article id %d"%article_id)
    article = Article.objects.get(id=article_id)

    return HttpResponse(json.dumps(article.__json__()))
