# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth.login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Disabled Account')
        else:
            return HttpResponse('Wrong ID/PW ')

    else:
        return redirect('home')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')
