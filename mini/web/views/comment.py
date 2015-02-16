# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from mini.web import forms as f
from mini.web import models as m
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404


@csrf_exempt
@login_required
def write(request, post_id=None):
    #ajax
    ctx = RequestContext(request)
    post = m.Post.objects.get(id=int(post_id))
    if request.method == 'POST':
        comment_form = f.CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.writer = request.user
            comment.post = post
            comment.save()

    return render_to_response('post/read.html', {'comment_form': f.CommentForm(), 'post': post}, ctx)


def read(request, post_id=None):
    #ajax
    ctx = RequestContext(request)
    post = m.Post.objects.get(id=int(post_id))
    comments = m.Comment.objects.filter(post=post).order_by('created')

    if request.is_ajax():
        return render_to_response('comment/read.html', {'post': post, 'comments': comments, 'with_layout': False}, ctx)
    else:
        return render_to_response('post/read.html', {'comment_form': f.CommentForm(), 'post': post}, ctx)
    #댓글 목록 가져오기


@csrf_exempt
@login_required
def update(request, comment_id=None):
    #ajax
    ctx = RequestContext(request)
    comment = m.Comment.objects.get(id=int(comment_id))
    writer = comment.writer
    post = comment.post

    if request.user != writer:
        return redirect('home')

    if request.method == 'POST':
        comment_form = f.CommentForm(request.POST, instance=comment)

        if comment_form.is_valid():
            comment_form.save()
            return redirect('post.read', post_id=post.id)

    else:
        comment_form = f.CommentForm(instance=comment)

    return render_to_response(
        'post/read.html', {'post': post, 'comment_update_form': comment_form,
                           'comment_form': f.CommentForm(), 'update_comment': comment}, ctx)


@csrf_exempt
@login_required
def delete(request, comment_id=None):
    comment = m.Comment.objects.get(id=int(comment_id))
    writer = comment.writer

    if request.user == writer:
        comment.delete()
    #댓글 삭제
    return redirect('post.read', post_id=comment.post.id)


@csrf_exempt
def like(request, comment_id=None):
    user = request.user
    comment = get_object_or_404(m.Comment, id=comment_id)

    user_liked, created = m.CommentLike.objects.get_or_create(comment=comment, user=user)

    if created is False:
        user_liked.delete()

    like_count = m.CommentLike.objects.filter(comment=comment).count()

    data = {'like_count': like_count}

    return HttpResponse(json.dumps(data))