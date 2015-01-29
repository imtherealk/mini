# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from mini.web import forms as f
from mini.web import models as m
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

            return redirect('/user/' + request.user.username + '/post/')

    else:
        post_form = f.PostForm()

        return render_to_response(
            'post/write.html', {'post_form': post_form}, ctx)


def read(request, post_id=None):
    ctx = RequestContext(request)
    post = m.Post.objects.get(id=int(post_id))
    comments = m.Comment.objects.filter(post=post).order_by('created')

    return render_to_response('post/read.html',
                              {'post': post, 'comments': comments,
                               'comment_form': f.CommentForm()}, ctx)


@csrf_exempt
@login_required
def update(request, post_id=None):
    ctx = RequestContext(request)
    post = m.Post.objects.get(id=int(post_id))
    writer = post.writer
    if request.user != writer:
        return redirect('post.read', post_id=post.id)

    updated = False

    if request.method == 'POST':
        post_form = f.PostForm(request.POST, request.FILES, instance=post)

        if post_form.is_valid():
            post_form.save()

            updated = True

    else:
        post_form = f.PostForm(instance=post)

    if updated:
        return redirect('post.read', post_id=post.id)

    return render_to_response(
        'post/read.html', {'post': post, 'post_form': post_form, 'update': True,
                           'comment_form': f.CommentForm()}, ctx)


@login_required
def delete(request, post_id=None):
    post = m.Post.objects.get(id=int(post_id))
    writer = post.writer
    if request.user == writer:
        post.delete()

    return redirect('timeline', username=writer.username)


def timeline(request, username=None):
    ctx = RequestContext(request)
    writer = m.MyUser.objects.get(username=username)
    posts = m.Post.objects.filter(writer=writer).order_by('-created')
    
    return render_to_response('post/timeline.html',
                              {'posts': posts, 'post_form': f.PostForm(),
                               'comment_form': f.CommentForm()}, ctx)


def newsfeed(request):
    pass


def like(request, post_id=None):
    pass