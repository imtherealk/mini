from mini.web import models as m
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def friend_request(request, to_username=None):
    ctx = RequestContext(request)

    if request.method == 'POST':
        to_user = m.MyUser.objects.get(username=to_username)
        from_user = request.user

        request, created = m.FriendRequest.objects.get_or_create(from_user=from_user,
                                                                 to_user=to_user)

        if created is False:
            pass

    return redirect('home')


@csrf_exempt
def accept(request, from_username=None):
    ctx = RequestContext(request)

    if request.method == 'POST':
        from_user = m.MyUser.objects.get(username=from_username)
        to_user = request.user
        request, created = m.Friend.objects.get_or_create(first_user=from_user, second_user=to_user)

        if created is False:
            pass

    return redirect('friend.read')


@csrf_exempt
def decline(request, from_username=None):
    from_user = m.MyUser.objects.get(username=from_username)
    to_user = request.user
    m.FriendRequest.objects.get(from_user=from_user, to_user=to_user).delete()

    return redirect('friend.request_list')


def read(request, username=None):
    ctx = RequestContext(request)
    user = m.MyUser.objects.get(username=username)
    friendships = m.Friend.objects.filter(Q(first_user=user) | Q(second_user=user))
    friends = m.MyUser.objects.filter(username=None)

    for f in friendships:
        friends = friends\
            | m.MyUser.objects.filter(Q(username=f.first_user.username) | Q(username=f.second_user.username))

    friends = friends.exclude(username=username)
    return render_to_response('friend/friends.html', {'friends': friends}, ctx)


def request_list(request):
    ctx = RequestContext(request)
    user = request.user
    requests = m.FriendRequest.objects.filter(to_user=user)

    return render_to_response('friend/request_list.html', {'requests': requests}, ctx)


def unfriend(request, to_username=None):
    user = request.user
    to_user = m.MyUser.objects.get(username=to_username)
    m.Friend.objects.get(first_user=user, second_user=to_user)

    return redirect('friend.read')