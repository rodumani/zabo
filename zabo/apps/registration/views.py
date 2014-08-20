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

# App library

def convert_str_to_date(str_date):
    try :
        return datetime.strptime(str_date, '%Y/%m/%d')
    except :
        return None

def convert_date_to_str(date):
    try :
        return datetime.strftime(date, '%Y/%m/%d')
    except :
        return None

def validate_article(category, title, start_date, end_date, activate, \
        comment, files):

    # check all parameter is set
    if title == '' :
        return {'status' : 400, 'msg' : 'Title field is blank'}

    # check category field value
    # XXX choice_list variable could be cached?
    choice_list = map(lambda x : x[0], Article._meta.get_field('category').choices)
    if category not in choice_list:
        return {'status' : 400, 'msg' : 'Category field value is not right'}

    # check date
    if (start_date == None or end_date == None):
        return {'status' : 400, 'msg' : 'Date field value is not right ' + \
                start_date_str + ', ' + end_date_str}
    if (start_date > end_date):
        return {'status' : 400, 'msg' : 'Start date cannot be after end date'}

    for afile in files :
        try :
            Image.open(files[afile]).verify()

        except IOError:
            return {'status' : 400, 'msg' : 'Poster image is not valid'}

    return None

# Page render function

@login_required
def new_registration(request):
    return render_to_response('new_registration.html', {
        'category_choice' : Article._meta.get_field('category').choices
        }, context_instance=RequestContext(request))

@login_required
def edit_registration(request, articleID):

    article = Article.objects.get(id=articleID)

    if (request.user != article.writer):
        return HttpResponse('User does not own the article', status=401)

    return render_to_response('edit_registration.html', {
        'category_choice' : Article._meta.get_field('category').choices,
        'articleID' : articleID,
        }, context_instance=RequestContext(request))

# API Call

@login_required
def add_article(request):

    category = int(request.POST['category'])
    title = request.POST.get('title', '').strip()
    start_date_str = request.POST.get('start_date', '').strip()
    end_date_str = request.POST.get('end_date', '').strip()
    activate_str = request.POST.get('activate', '').strip()
    comment = request.POST['comment'].strip()
    files = request.FILES
    user = request.user
    
    start_date = convert_str_to_date(start_date_str)
    end_date = convert_str_to_date(end_date_str)
    activate = True if activate_str == 'on' else False

    validate = validate_article(category, title, start_date, end_date, \
            activate_str, comment, files)
    if validate != None:
        return HttpResponse(validate['msg'], status=validate['status'])

    # create board instance and save
    new_article = Article.objects.create(writer=user, title=title, \
            category=category, start_datetime=start_date, \
            end_datetime=end_date, activate=activate, comment=comment)

    number_of_files = len(files)
    file_to_save = []
    if (number_of_files >= 1):
        main_file = files['main0']
        main_poster = Poster(belong_article_main=new_article, picture=main_file)
        file_to_save.append(main_poster)

        if (number_of_files >= 2):
            for count in range(0, number_of_files - 1):
                sub_file = files['sub' + str(count)]
                sub_poster = Poster(belong_article_sub=new_article, picture=sub_file)
                file_to_save.append(sub_poster)

    file_saved = map(lambda x : x.save(), file_to_save)
    return HttpResponse("ADD ARTICLE")

@login_required
def edit_article(request, articleID):

    article = Article.objects.get(id=articleID)

    if (request.user != article.writer):
        return HttpResponse('User does not own the article', status=401)

    category = int(request.POST['category'])
    title = request.POST.get('title', '').strip()
    start_date_str = request.POST.get('start_date', '').strip()
    end_date_str = request.POST.get('end_date', '').strip()
    activate_str = request.POST.get('activate', '').strip()
    comment = request.POST['comment'].strip()
    files = request.FILES
    user = request.user

    start_date = convert_str_to_date(start_date_str)
    end_date = convert_str_to_date(end_date_str)
    activate = True if activate_str == 'on' else False

    validate = validate_article(category, title, start_date, end_date, \
            activate_str, comment, files)

    if validate != None:
        return HttpResponse(validate['msg'], status=validate['status'])

    article.category = category
    article.title = title
    article.start_date = start_date
    article.end_date = end_date
    article.activate = activate
    article.comment = comment

    article.save();

    file_to_save = []
    # TODO update article posters...
    for afile in files :
        if afile == "main0":
            article.main_poster.picture = files[afile]
            file_to_save.append(article.main_poster)
        else :
            index = int(afile[3:])
            if (index < article.sub_poster.length) :
                article.sub_poster[index].poster.picture = files[afile]
                file_to_save.append(article.sub_poster[index])
            else :
                sub_poster = Poster(belong_article_sub=article, picture=files[afile])
                file_to_save.append(sub_poster)

    file_saved = map(lambda x : x.save(), file_to_save)

    return HttpResponse("EDIT ARTICLE")

def remove_article(request):
    return HttpResponse("REMOVE ARTICLE")
