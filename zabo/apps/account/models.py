# -*- coding: utf-8
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import os

DEPARTMENT_CHOICES = (
    (1, u'IT분과'),
    (2, u'체육분과'),
)

class UserProfile(models.Model):
    # profile of user
    user = models.OneToOneField(User, related_name="profile")

    club_name = models.CharField(max_length = 50)
    club_name_en = models.CharField(max_length = 50)
    profile_image = models.ImageField(upload_to='profile/', default='profile/no-img.jpg')
    department = models.SmallIntegerField(choices=DEPARTMENT_CHOICES)
    club_comment = models.TextField()

    def __json__(self) :
        return {
            'username' : self.user.username,
            'club_name' : self.club_name,
            'club_name_en' : self.club_name_en,
            'profile' : {
                    'file' : os.path.basename(self.profile_image.name),
                    'url' : self.profile_image.url,
                },
            'department' : self.get_department_display(),
            'club_comment' : self.club_comment,
            }
        

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('club_name', 'club_name_en')

admin.site.register(UserProfile, UserProfileAdmin)
