# -*- coding: utf-8 -*-
import functools
from django.template import RequestContext
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from mini.web import forms as f
from mini.web import models as m
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings


def home(request):
    if request.user.is_authenticated():
        tpl = loader.get_template('newsfeed.html')
        ctx = Context({'request_user': request.user})
        return HttpResponse(tpl.render(ctx))

    user_form = f.UserForm()
    profile_form = f.UserProfileForm()
    tpl = loader.get_template('home.html')
    ctx = Context({'user_form': user_form, 'profile_form': profile_form})

    return HttpResponse(tpl.render(ctx))


@csrf_exempt
def register(request):
    if request.user.is_authenticated():
        return redirect('home')

    ctx = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = f.UserForm(request.POST)
        profile_form = f.UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            pass

    else:
        user_form = f.UserForm()
        profile_form = f.UserProfileForm()

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
    user = m.User.objects.get(username=username)

    if request_user == user:
        me = True
    else:
        me = False

    profile = m.UserProfile.objects.get_or_create(user=user)[0]
    rel_status = profile.get_relationship_status_display()
    return render_to_response('profile.html', {'profile': profile,
                                               'request_user': request_user,
                                               'rel_status': rel_status,
                                               'me': me})


@csrf_exempt
@login_required
def profile_update(request, username=None):
    ctx = RequestContext(request)
    user = m.User.objects.get(username=username)
    if request.user != user:
        return redirect('home')
    profile = m.UserProfile.objects.get(user=user)

    updated = False

    if request.method == 'POST':
        edit_u_form = f.EditUserForm(request.POST, instance=user)
        edit_p_form = f.EditProfileForm(request.POST, request.FILES,
                                        instance=profile)

        if edit_u_form.is_valid() and edit_p_form.is_valid():
            edit_u_form.save()
            edit_p_form.save()
            if 'profile_image' not in request.FILES \
                    and profile.profile_image is None:
                profile.profile_image = 'sandbox/profile-images/default.png'
                profile.save()

            updated = True

    else:
        edit_u_form = f.EditUserForm(instance=user)
        edit_p_form = f.EditProfileForm(instance=profile)

    if updated:
        return redirect('/user/'+username)

    return render_to_response(
        'edit_profile.html', {'profile': profile,
                              'edit_u_form': edit_u_form,
                              'edit_p_form': edit_p_form,
                              'request_user': request.user}, ctx)


@csrf_exempt
@login_required
def write_post(request):
    ctx = RequestContext(request)

    if request.method == 'POST':
        post_form = f.PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.writer = request.user
            post.save()

            return redirect('/user/'+request.user.username+'/post/')

    else:
        post_form = f.PostForm()

        return render_to_response(
            'post_form.html', {'post_form': post_form,
                               'request_user': request.user}, ctx)


def read(request, post_id=None):
    post = m.Post.objects.get(id=int(post_id))
    writer = post.writer
    profile = m.UserProfile.objects.get(user=writer)

    tpl = loader.get_template('post.html')
    ctx = Context({
        'post': post,
        'profile': profile,
        'request_user': request.user
    })
    return HttpResponse(tpl.render(ctx))


def timeline(request, username=None):
    writer = m.User.objects.get(username=username)
    profile = m.UserProfile.objects.get(user=writer)
    posts = m.Post.objects.filter(writer=writer).order_by('-created')

    tpl = loader.get_template('post_list.html')
    ctx = Context({
        'posts': posts,
        'request_user': request.user,
        'profile': profile,
        'post_form': f.PostForm()
    })
    return HttpResponse(tpl.render(ctx))


def newsfeed(request):
    pass
