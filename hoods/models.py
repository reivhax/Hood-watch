# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Neighbourhood(models.Model):
    Name = models.TextField()
    display = models.ImageField(upload_to='groups/', default='groups/group.png')
    admin = models.ForeignKey("Profile", related_name='hoods')
    description = models.TextField(default='Random group')
    police = models.TextField(default="999")
    health = models.TextField(default="213")

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


class Business(models.Model):
    Name = models.TextField()
    owner = models.ForeignKey(Profile)
    show_my_email = models.BooleanField(default=True)
    description = models.TextField(default='Local business')
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='biashara')

    @property
    def email(self):
        return self.owner.user.email


class Post(models.Model):
    user = models.ForeignKey(Profile)
    Text = models.TextField()
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='posts')
