# -*- coding: utf-8 -*-
from mini.web import forms as f
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect


def home(request):
    ctx = RequestContext(request)
    if request.user.is_authenticated():
        return redirect('newsfeed')

    return render_to_response('home.html', {'user_form': f.UserForm(),
                                            'login_form': f.LoginForm()}, ctx)
