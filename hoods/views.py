# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm, HoodForm, BizForm, PostForm
from .models import Neighbourhood


@login_required
def home(request):
    return redirect(myprofile);


@login_required
def myprofile(request):
    return render(request, 'myprofile.html')


@login_required
def myhood(request):
    return render(request, 'myhood.html')
@login_required
def create_neighbourhood(request):
    if request.method == 'POST':
        hood_form = HoodForm(request.POST, request.FILES)
        if hood_form.is_valid():
            hood = hood_form.save(commit=False)
            hood.admin = request.user.profile
            request.user.profile.save()
            hood.save()
            return redirect(neighbourhoods)
    else:
        hood_form = HoodForm()
    return render(request, 'newneighbourhood.html', locals())
