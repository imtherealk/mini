# -*- coding: utf-8 -*-
import functools
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from mini.web import forms as f
from mini.web import models as m
from django.contrib.auth.decorators import login_required


@csrf_exempt
def register(request):
    if request.user.is_authenticated():
        return redirect('home')

    ctx = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = f.UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            pass

    else:
        user_form = f.UserForm()

    return render_to_response(
        'home.html', {'user_form': user_form, 'registered': registered, 'login_form': f.LoginForm()}, ctx)


@csrf_exempt
@login_required
def unregister(request, username=None):
    request.user.delete()
    return redirect('home')


def read(request, username=None):
    user = m.MyUser.objects.get(username=username)

    if request.user == user:
        me = True
    else:
        me = False

    return render_to_response('user/profile.html',
                              {'profile': user,
                               'me': me}, RequestContext(request))


@csrf_exempt
@login_required
def update(request, username=None):
    ctx = RequestContext(request)
    user = m.MyUser.objects.get(username=username)
    if request.user != user:
        return redirect('home')

    updated = False

    if request.method == 'POST':
        edit_u_form = f.EditUserForm(request.POST, request.FILES, instance=user)

        if edit_u_form.is_valid():
            edit_u_form.save()
            if 'profile_image' not in request.FILES \
                    and user.profile_image is None:
                user.profile_image = 'static/images/default_profile.png'
                user.save()

            updated = True

    else:
        edit_u_form = f.EditUserForm(instance=user)

    if updated:
        return redirect('/user/'+username)

    return render_to_response(
        'user/update.html', {'profile': user, 'edit_u_form': edit_u_form}, ctx)
