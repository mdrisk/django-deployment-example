# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)

    #addons
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)
    #be sure to have Pillow installed for python image dealings


    def __str__(self):
        return self.user.username
