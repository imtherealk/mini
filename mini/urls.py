from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mini.web.views.home', name='home'),
    url(r'^user/$', 'mini.web.views.register'),
    url(r'^user/(?P<username>\w+)/delete', 'mini.web.views.unregister'),
    url(r'^user/(?P<username>\w+)/$', 'mini.web.views.user_profile'),
    url(r'^login', 'mini.web.views.log_in'),
    url(r'^logout', 'mini.web.views.log_out'),
    url(r'^admin/', include(admin.site.urls)),
)
