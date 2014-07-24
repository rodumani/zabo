# -*- coding: utf-8
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.template import RequestContext
from django.shortcuts import render_to_response, HttpResponseRedirect

from django import template

from django.contrib.auth.models import User
from zabo.apps.board.models import Article
from datetime import datetime

def new_registration(request):
    return render_to_response('new_registration.html', {}, 
                context_instance=RequestContext(request))

def add_board(request):

    category = 1
    title = "title"
    start_date = datetime.now()
    end_date = datetime.now()
    activate = True
    comment = "comment"
    files = []
    user = request.user

    if user.is_authenticated():
        user = User.objects.get(id=1)
        print user

    # TODO validation check
    new_article = Article.objects.create(writer=user, title=title, \
            category=category, start_datetime=start_date, end_datetime=end_date, \
            activate=activate, comment=comment)

    # create board instance and save
    number_of_files = len(files)
    if (number_of_files == 0):
        pass
    elif (number_of_files > 1):
        main_file = files[0]
        sub_files = files[1:]

        # TODO create main poster instance
        main_poster = Poster.objects.create(belong_article_main=new_article)
        
        for sub_file in sub_files:
            # TODO create sub poster instances
            new_post = Poster.objects.create(belong_article_sub=new_article)

    # return succes page
    # return fail page

    return HttpResponse("ADD BOARD")

def edit_board(request):
    return HttpResponse("EDIT BOARD")

def remove_board(request):
    return HttpResponse("REMOVE BOARD")
