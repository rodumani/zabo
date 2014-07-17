# -*- coding: utf-8
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.template import RequestContext
from django.shortcuts import render_to_response, HttpResponseRedirect

from django import template

def new_registration(request):
    return render_to_response('new_registration.html', {}, 
                context_instance=RequestContext(request))

def add_board(request):

    category = ""
    title = ""
    description = ""
    start_date = ""
    end_date = ""
    activate = True
    files = []

    # validation check
    # create board instance and save

    # return succes page
    # return fail page

    return HttpResponse("ADD BOARD")

def edit_board(request):
    return HttpResponse("EDIT BOARD")

def remove_board(request):
    return HttpResponse("REMOVE BOARD")
