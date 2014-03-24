from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import os


# Create your models here.

class Article(models.Model):
    """ Article that is linked with zabo """
    writer = models.ForeignKey(User)
    written_datetime = models.DateTimeField(auto_now=True)
    comment = models.TextField()

class Poster(models.Model):
    """ Image field of zabo """
    picture = models.ImageField(upload_to='pictures/', default='pictures/no-img.jpg')
    article = models.ForeignKey(Article, related_name='poster')
    def __unicode__(self):
        """show picture's name"""
        return os.path.basename(self.picture.name)
    def name(self):
        """returns itself"""
        return self

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('writer', 'written_datetime', 'comment')

class PosterAdmin(admin.ModelAdmin):
    list_display = ('name', 'article')

admin.site.register(Poster, PosterAdmin)
admin.site.register(Article, ArticleAdmin)
