# -*- coding: utf-8 -*-
import functools
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from mini.web.forms import UserForm, UserProfileForm
from mini.web.models import *
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings


def home(request):
    if request.user.is_authenticated():
        tpl = loader.get_template('newsfeed.html')
        ctx = Context({'request_user': request.user})
        return HttpResponse(tpl.render(ctx))

    user_form = UserForm()
    profile_form = UserProfileForm()
    tpl = loader.get_template('home.html')
    ctx = Context({'user_form': user_form, 'profile_form': profile_form})

    return HttpResponse(tpl.render(ctx))


@csrf_exempt
def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    ctx = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']

            profile.save()
            registered = True

        else:
            pass

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
        'home.html', {'user_form': user_form, 'profile_form': profile_form,
        'registered': registered}, ctx)


@csrf_exempt
@login_required
def unregister(request, username=None):
    request.user.delete()
    return redirect('home')


@csrf_exempt
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Disabled Account')
        else:
            return HttpResponse('Wrong ID/PW ')

    else:
        return redirect('home')


@login_required
def log_out(request):
    logout(request)
    return redirect('home')


@login_required
def user_profile(request, username=None):
    request_user = request.user
    profile_user = User.objects.get(username=username)
    return render_to_response('profile.html', {'profile_user': profile_user,
                                               'request_user': request_user})
