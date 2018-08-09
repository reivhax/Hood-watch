# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm, HoodForm, BizForm, PostForm
from .models import Neighbourhood


@login_required
def home(request):
    return redirect(myprofile);

