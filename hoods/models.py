# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Neighbourhood(models.Model):
    Name = models.TextField()
    display = models.ImageField(upload_to='groups/', default='groups/group.png')
    admin = models.ForeignKey("Profile", related_name='hoods')
    description = models.TextField(default='Random group')

    def __str__(self):
        return self.Name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.TextField(default="Anonymous")
    profile_picture = models.ImageField(upload_to='users/', default='users/user.png')
    bio = models.TextField(default="I'm using hoodwatch")
    neighbourhood = models.ForeignKey(Neighbourhood, blank=True, null=True, related_name='people')

    def __str__(self):
        return f'Profile {self.user.username}'
