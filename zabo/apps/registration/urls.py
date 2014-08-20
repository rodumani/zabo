from django.conf.urls import *
from zabo.apps.registration import views

urlpatterns = patterns('',
    url(ur'^$', views.new_registration),
    url(ur'^(?P<articleID>[0-9]+)/$', views.edit_registration),
    url(ur'^edit/(?P<articleID>[0-9]+)/$', views.edit_article),
    url(ur'^add/$', views.add_article),
)
