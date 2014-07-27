from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    # profile of user
    user = models.OneToOneField(User, related_name="profile")

    club_name = models.CharField(max_length = 50)
    club_name_en = models.CharField(max_length = 50)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('club_name', 'club_name_en')

admin.site.register(UserProfile, UserProfileAdmin)
