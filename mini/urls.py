from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mini.web.views.home.home', name='home'),
    url(r'^user/$', 'mini.web.views.user.register'),
    url(r'^user/(?P<username>\w+)/delete', 'mini.web.views.user.unregister'),
    url(r'^user/(?P<username>\w+)/$', 'mini.web.views.user.read'),
    url(r'^user/(?P<username>\w+)/update', 'mini.web.views.user.update'),
    url(r'^login', 'mini.web.views.auth.log_in'),
    url(r'^logout', 'mini.web.views.auth.log_out'),
    url(r'^post/$', 'mini.web.views.post.write'),
    url(r'^post/(?P<post_id>\d+)/$', 'mini.web.views.post.read'),
    url(r'^user/(?P<username>\w+)/post', 'mini.web.views.post.timeline'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT})
)

