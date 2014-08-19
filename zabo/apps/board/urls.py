from django.conf.urls import *
from zabo.apps.board import views

urlpatterns = patterns('',
    url(r'^get_detail/$', views.get_detail),
)
