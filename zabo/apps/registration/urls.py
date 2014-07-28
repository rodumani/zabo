from django.conf.urls import *
from zabo.apps.registration import views

urlpatterns = patterns('',
    url(ur'^$', views.new_registration),
    url(ur'^add_board/', views.add_board),
)
