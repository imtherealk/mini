from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
urlpatterns = patterns(
    '',

    # User
    url(r'^$', 'mini.web.views.home.home', name='home'),
    url(r'^user/$', 'mini.web.views.user.register', name='user.register'),
    url(r'^user/(?P<username>\w+)/$', 'mini.web.views.user.read', name='user.read'),
    url(r'^user/(?P<username>\w+)/update', 'mini.web.views.user.update', name='user.update'),
    url(r'^user/(?P<username>\w+)/delete', 'mini.web.views.user.unregister', name='user.delete'),

    # Auth
    url(r'^login', 'mini.web.views.auth.login', name='login'),
    url(r'^logout', 'mini.web.views.auth.logout', name='logout'),

    # Post
    url(r'^post/$', 'mini.web.views.post.write', name='post.write'),
    url(r'^post/(?P<post_id>\d+)/$', 'mini.web.views.post.read', name='post.read'),
    url(r'^user/(?P<username>\w+)/post', 'mini.web.views.post.timeline', name='timeline'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


