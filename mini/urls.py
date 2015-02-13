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
    url(r'^newsfeed/$', 'mini.web.views.post.newsfeed', name='newsfeed'),
    url(r'^post/(?P<post_id>\d+)/update', 'mini.web.views.post.update', name='post.update'),
    url(r'^post/(?P<post_id>\d+)/delete', 'mini.web.views.post.delete', name='post.delete'),
    url(r'^post/(?P<post_id>\d+)/like', 'mini.web.views.post.like', name='post.like'),

    # Comment
    url(r'^post/(?P<post_id>\d+)/comment/write/$', 'mini.web.views.comment.write', name='comment.write'),
    url(r'^post/(?P<post_id>\d+)/comment/$', 'mini.web.views.comment.read', name='comment.read'),
    url(r'^comment/(?P<comment_id>\d+)/update', 'mini.web.views.comment.update', name='comment.update'),
    url(r'^comment/(?P<comment_id>\d+)/delete', 'mini.web.views.comment.delete', name='comment.delete'),


    # Friend
    url(r'^friendrequest/(?P<to_username>\w+)/$', 'mini.web.views.friend.friend_request', name='friend.request'),
    url(r'^user/(?P<username>\w+)/friend/$', 'mini.web.views.friend.read', name='friend.read'),
    url(r'^friendrequest/$', 'mini.web.views.friend.request_list', name='friend.request_list'),
    url(r'^friend/friendrequest/(?P<from_username>\w+)/$', 'mini.web.views.friend.accept', name='friend.accept'),
    url(r'^friendrequest/(?P<from_username>\w+)/delete', 'mini.web.views.friend.decline', name='friend.decline'),
    url(r'^friend/(?P<other_username>\w+)/delete', 'mini.web.views.friend.unfriend', name='friend.delete'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


