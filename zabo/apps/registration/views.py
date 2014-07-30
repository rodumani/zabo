# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.template import RequestContext
from django.shortcuts import render_to_response, HttpResponseRedirect
from django import template

from zabo.apps.board.models import Article, Poster
from datetime import datetime
from PIL import Image


def convert_str_to_date(str_date):
    try :
        return datetime.strptime(str_date, '%Y/%m/%d')
    except :
        return None

@login_required
def new_registration(request):
    return render_to_response('new_registration.html', {
        'category_choice' : Article._meta.get_field('category').choices
        }, context_instance=RequestContext(request))

@login_required
def add_board(request):

    category = int(request.POST['category'])
    title = request.POST.get('title', '').strip()
    start_date_str = request.POST.get('start_date', '').strip()
    end_date_str = request.POST.get('end_date', '').strip()
    activate_str = request.POST.get('activate', '').strip()
    comment = request.POST['comment'].strip()
    files = request.FILES
    user = request.user

    # parameter check
    if title == '' or start_date_str == '' or end_date_str == '' or \
            activate_str == '':
        return HttpResponseBadRequest('Not enough parameter')

    # category check
    choice_list = map(lambda x : x[0], Article._meta.get_field('category').choices)
    if category not in choice_list:
        return HttpResponseBadRequest('Category field value is not right')

    # start, end date check ex)2014/07/27
    start_date = convert_str_to_date(start_date_str)
    end_date = convert_str_to_date(end_date_str)
    if (start_date == None or end_date == None):
        return HttpResponseBadRequest('Date field value is not right ' + \
                start_date_str + ', ' + end_date_str)
    if (start_date > end_date):
        return HttpResponseBadRequest('Start date cannot be after end date')

    # check activate
    activate = True if activate_str == 'on' else False

    # create board instance and save
    new_article = Article.objects.create(writer=user, title=title, \
            category=category, start_datetime=start_date, \
            end_datetime=end_date, activate=activate, comment=comment)

    number_of_files = len(files)
    file_to_save = []
    if (number_of_files >= 1):
        try :
            main_file = files['main']
            main_poster = Poster(belong_article_main=new_article, picture=main_file)
            Image.open(main_file).verify()
            file_to_save.append(main_poster)

            if (number_of_files >= 2):
                for count in range(1, number_of_files):
                    sub_file = files['sub' + str(count)]
                    Image.open(sub_file).verify()
                    sub_poster = Poster(belong_article_sub=new_article, picture=sub_file)
                    file_to_save.append(sub_poster)

        except IOError:
            return HttpResponseBadRequest('Poster image is not valid')

    file_saved = map(lambda x : x.save(), file_to_save)
    return HttpResponse("ADD BOARD")

def edit_board(request):
    return HttpResponse("EDIT BOARD")

def remove_board(request):
    return HttpResponse("REMOVE BOARD")
