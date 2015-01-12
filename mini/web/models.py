import os

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Model(models.Model):
    def __repr__(self):
        module_name = __name__
        class_name = type(self).__name__
        return module_name + '.' + class_name + '(%s)' % self.id

    def __str__(self):
        return repr(self)

    class Meta(object):
        abstract = True


class UserProfile(Model):
    RELATIONSHIP_STATUSES = (
        ('y', 'Yes'),
        ('n', 'No'),
        ('m', 'Married'),
    )

    user = models.ForeignKey(User, unique=True)
    relationship_status = models.CharField(max_length=1, null=True,
                                           choices=RELATIONSHIP_STATUSES)
    IMAGE_DIR = os.path.join(settings.SANDBOX, 'profile-images')
    profile_image = models.ImageField(upload_to=IMAGE_DIR, null=True,
                                      blank=True)


class Post(Model):
    writer = models.ForeignKey(User)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    IMAGE_DIR = os.path.join(settings.SANDBOX, 'post-images')
    image = models.ImageField(upload_to=IMAGE_DIR, null=True, blank=True)


class Comment(Model):
    writer = models.ForeignKey(User)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)


class Friend(Model):
    first_user = models.ForeignKey(User, related_name='+')
    second_user = models.ForeignKey(User, related_name='+')
    created = models.DateTimeField(auto_now_add=True)


class FriendRequest(Model):
    from_user = models.ForeignKey(User, related_name='+')
    to_user = models.ForeignKey(User, related_name='+')
    created = models.DateTimeField(auto_now_add=True)


class PostLike(Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)


class CommentLike(Model):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)
