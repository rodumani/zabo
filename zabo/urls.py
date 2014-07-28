from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zabo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/', include('zabo.apps.registration.urls')),
    url(r'^login/', 'zabo.apps.account.views.login'),
    url(r'^logout/', 'zabo.apps.account.views.logout'),
    url(r'^main/', 'zabo.apps.board.views.view'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    url(r'^imagefit/', include('imagefit.urls')),
)

