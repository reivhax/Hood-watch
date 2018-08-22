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
def neighbourhoods(request):
    hoods = Neighbourhood.objects.all()
    return render(request, 'neighbourhoods.html', locals())


@login_required
def join_neighbourhood(request, neigh_id):
    hood = get_object_or_404(Neighbourhood, pk=neigh_id)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    return redirect(neighbourhoods)


@login_required
def leave_neighbourhood(request, neigh_id):
    hood = get_object_or_404(Neighbourhood, pk=neigh_id)
    if request.user.profile.neighbourhood == hood:
        request.user.profile.neighbourhood=None
        request.user.profile.save()
    return redirect(neighbourhoods)


@login_required
def delete_neighbourhood(request, neigh_id):
    hood = get_object_or_404(request.user.profile.hoods, pk=neigh_id)
    for member in hood.people.all():
        member.neighbourhood = None
        member.save()
    request.user.profile.hoods.filter(pk=neigh_id).delete()
    return redirect(myprofile)


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


@login_required
def create_biz(request):
    if request.method == 'POST':
        biz_form = BizForm(request.POST, request.FILES)
        if biz_form.is_valid():
            biz = biz_form.save(commit=False)
            biz.owner = request.user.profile
            biz.neighbourhood = request.user.profile.neighbourhood
            biz.save()
            return redirect(myhood)
    else:
        biz_form = BizForm()
    return render(request, 'newbiz.html', locals())


@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user.profile
            post.neighbourhood = request.user.profile.neighbourhood
            post.save()
            return redirect(myhood)
    else:
        post_form = PostForm()
    return render(request, 'newpost.html', locals())


@login_required
def edit_neighbourhood(request, neigh_id):
    hood = get_object_or_404(request.user.profile.hoods, pk=neigh_id)
    if request.method == 'POST':
        hood_form = HoodForm(request.POST, request.FILES, instance=hood)
        if hood_form.is_valid():
            hood = hood_form.save(commit=False)
            hood.admin = request.user.profile
            request.user.profile.save()
            hood.save()
            return redirect(myhood)
    else:
        hood_form = HoodForm(instance=hood)
    return render(request, 'newneighbourhood.html', locals())


@login_required
def create_profile(request):
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profileform.is_valid():
            profileform.save()
            return redirect(myprofile)
    else:
        profileform = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', locals())


@login_required
def search_(): pass
