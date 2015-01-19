# -*- coding: utf-8 -*-
from django.http import HttpResponse
from mini.web import forms as f
from django.template import Context, loader


def home(request):
    if request.user.is_authenticated():
        tpl = loader.get_template('post/newsfeed.html')
        ctx = Context({'request_user': request.user})
        return HttpResponse(tpl.render(ctx))

    user_form = f.UserForm()
    profile_form = f.UserProfileForm()
    tpl = loader.get_template('home.html')
    ctx = Context({'user_form': user_form, 'profile_form': profile_form})

    return HttpResponse(tpl.render(ctx))
