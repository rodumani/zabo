# -*- coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import os


# Create your models here.

CATEGORY_CHOICES = (
    (1, u'신입생 모집'),
    (2, u'동아리 행사'),
)

class Article(models.Model):
    """ Article that is linked with zabo """
    writer = models.ForeignKey(User)
    title = models.CharField(max_length = 128)
    category = models.SmallIntegerField(choices=CATEGORY_CHOICES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    activate = models.BooleanField()
    comment = models.TextField()

    def __json__(self):

        sub_pictures = [ poster.__json__() for poster in self.sub_poster.all()]

        return {
            'category' : self.get_category_display(),
            'title' : self.title,
            'writer' : self.writer.profile.__json__(),
            'main_picture' : {
                'file' : os.path.basename(self.main_poster.picture.name),
                'url' : self.main_poster.picture.url 
                },    
            'sub_pictures' : sub_pictures,
            'start_time' : str(self.start_datetime.date()),
            'end_time' : str(self.end_datetime.date()),
            'comment' : self.comment
            }


class Poster(models.Model):
    """ Image field of zabo """
    picture = models.ImageField(upload_to='pictures/', default='pictures/no-img.jpg')
    belong_article_sub = models.ForeignKey(Article, related_name='sub_poster', null=True, blank=True)
    belong_article_main = models.OneToOneField(Article, related_name='main_poster', null=True, blank=True)
    def __unicode__(self):
        """show picture's name"""
        return os.path.basename(self.picture.name)
    def name(self):
        """returns itself"""
        return self
    def __json__(self):
        return {
            'file' : os.path.basename(self.picture.name),
            'url' : self.picture.url,
            }

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('writer', 'title', 'category', 'start_datetime', 'end_datetime', 'activate', 'comment')

class PosterAdmin(admin.ModelAdmin):
    list_display = ('name', 'belong_article_sub', 'belong_article_main')

admin.site.register(Poster, PosterAdmin)
admin.site.register(Article, ArticleAdmin)
