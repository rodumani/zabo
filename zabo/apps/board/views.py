#-*- coding: utf-8 -*-
""" 자보 리스트 보여주기 기능 구현 """
from models import Article, Poster
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from zabo.apps.account.models import UserProfile
from django.core.serializers.json import DjangoJSONEncoder
import os
import json

# Create your views here.

MAX_HEIGHT = 180
PAGE_WIDTH = 984
MAX_WIDTH = PAGE_WIDTH * 0.9 # For good look
def determine_space(N, length):
    remaining_width = int(PAGE_WIDTH - length) - 1
    space_n = N - 1
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
    club = UserProfile.objects.filter(Q(club_name__iexact=query) | Q(club_name_en__iexact=query))
    if not len(club)==1:
        #TODO show search result
        return redirect('/')
    return redirect('/club/'+club[0].club_name_en)

def get_ctx(articles):
    """
        return context in redirect
        articles : want to show articles
    """

    all = []
    l = []
    length = 0
    minimum = MAX_WIDTH
    for article in articles:
        picture = article.main_poster.picture
        new_width = MAX_HEIGHT * picture.width / picture.height
        if length + new_width > MAX_WIDTH:
            space = determine_space(len(l), length)
            minimum = min(minimum, space[0])
            line = []
            for i in range(len(l)): # determine the margin
                line.append([l[i][0], l[i][1], l[i][2], space[i]])
            all.append(line)
            l = []
            length = 0
        l.append((picture.url, article.writer, article.id))
        length += new_width

    if length != 0:
        line = []
        for i in range(len(l)):
            if i == len(l) - 1:
                line.append([l[i][0], l[i][1], l[i][2], 0])
            else:
                line.append([l[i][0], l[i][1], l[i][2], minimum])
        all.append(line)

    page_template = 'board/view_page.html'
    ctx = {'chosen':all,
            'page_template':page_template,
            'picture_height':MAX_HEIGHT,
            }
    return ctx

def get_detail(request):
    print request
    article_id = request.GET['article_id']
    
    if not Article.objects.filter(id=article_id).exists():
        raise ValidationError("no article id %d"%article_id)
    article = Article.objects.get(id=article_id)
    sub_pictures = [poster.picture.url for poster in article.sub_poster.all()]
    return HttpResponse(json.dumps({
        'title' : '[' + article.get_category_display() + '] ' + article.title,
        'writer_name' : article.writer.profile.club_name,
        'main_picture' : article.main_poster.picture.url,
        'sub_pictrues' : sub_pictures,
        'start_time' : article.start_datetime.date(),
        'end_time' : article.end_datetime.date(),
        'content' : article.comment
    }, cls=DjangoJSONEncoder))
