# -*- coding: utf-8 -*-
"""account view - login, logout"""
## Create your views here.
from django.shortcuts import redirect, render_to_response
from django.contrib import auth
from django.template import RequestContext

def login(request):
    """
        login 기능 구현
        request : Http request
    """
    next_url = request.GET.get('next', '/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect(request.POST['next'])
        else:
            error = "Invalid login"
        return render_to_response('login.html', {
            'next':next_url,
            'error':error}, context_instance=RequestContext(request))
    return render_to_response('login.html',
            {'next':next_url}, context_instance=RequestContext(request))
