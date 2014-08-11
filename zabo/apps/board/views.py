#-*- coding: utf-8 -*-
""" 자보 리스트 보여주기 기능 구현 """
from models import Article, Poster
from django.http import HttpResponse
from django.shortcuts import redirect, render
from zabo.apps.account.models import UserProfile
import os

# Create your views here.

MAX_HEIGHT = 240
PAGE_WIDTH = 1024
MAX_WIDTH = PAGE_WIDTH * 0.9 # For good look
def determine_space(N, length):
    remaining_width = int(MAX_WIDTH - length)
    space_n = 3 * N - 1
    space_width = remaining_width / space_n
    space_interval = [space_width] * (space_n - (remaining_width % N)) 
    space_interval += [space_width + 1] * (remaining_width % N)
    space_interval += [0]
    return space_interval

def view(request):
    """
        자보 리스트를 보여준다.
        request : http request
        page : page number
    """
    if request.method == 'POST':
        pass
    no_of_articles = Article.objects.count()
    articles = Article.objects.all().order_by('?')

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
                line.append([l[i], space[i*3], space[i*3+1], space[i*3+2]])
            all.append(line)
            l = []
            length = 0
        l.append(picture.url)
        length += new_width

    if length != 0:
        line = []
        for i in range(len(l)):
            line.append([l[i], 0, 0, 10])
        all.append(line)

    template = 'board/view.html'
    page_template = 'board/view_page.html'
    ctx = {'chosen':all,
            'no_of_articles':no_of_articles,
            'page_template':page_template,
            'picture_height':MAX_HEIGHT,
            }
    if request.is_ajax():
        template = page_template

    return render(request, template, ctx)

def category(request, category_num):
    """
        request : http request
        page : page number
    """
    if request.method == 'POST':
        pass
    no_of_articles = Article.objects.count()
    category = int(category_num)
    articles = Article.objects.filter(category=category)
    template = 'board/view.html'
    page_template = 'board/view_page.html'
    ctx = {'chosen':articles,
            'no_of_articles':no_of_articles,
            'page_template':page_template,
            }
    if request.is_ajax():
        template = page_template

    return render(request, template, ctx)

def search(request):
    query = request.GET.get('query', '')
    club = UserProfile.objects.filter(club_name_en=query)
    if not club:
        #TODO show search result
        return redirect('/')
    return redirect('/club/'+query)
