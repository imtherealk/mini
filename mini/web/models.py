import os

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class UserProfile(models.Model):
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


class Post(models.Model):
    writer = models.ForeignKey(User)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    IMAGE_DIR = os.path.join(settings.SANDBOX, 'post-images')
    image = models.ImageField(upload_to=IMAGE_DIR, null=True, blank=True)


class Comment(models.Model):
    writer = models.ForeignKey(User)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)


class Friend(models.Model):
    first_user = models.ForeignKey(User, related_name='+')
    second_user = models.ForeignKey(User, related_name='+')
    created = models.DateTimeField(auto_now_add=True)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='+')
    to_user = models.ForeignKey(User, related_name='+')
    created = models.DateTimeField(auto_now_add=True)


class PostLike(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)


class CommentLike(models.Model):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)
