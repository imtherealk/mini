# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from mini.web import forms as f
from mini.web import models as m
from django.template import Context, loader
from django.contrib.auth.decorators import login_required


@csrf_exempt
@login_required
def write(request):
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
            'post/write.html', {'post_form': post_form,
                                'request_user': request.user}, ctx)


def read(request, post_id=None):
    post = m.Post.objects.get(id=int(post_id))
    writer = post.writer
    profile = m.UserProfile.objects.get(user=writer)

    tpl = loader.get_template('post/read.html')
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

    tpl = loader.get_template('post/timeline.html')
    ctx = Context({
        'posts': posts,
        'request_user': request.user,
        'profile': profile,
        'post_form': f.PostForm()
    })
    return HttpResponse(tpl.render(ctx))


def newsfeed(request):
    pass