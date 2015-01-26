from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Model(models.Model):
    def __repr__(self):
        module_name = __name__
        class_name = type(self).__name__
        return module_name + '.' + class_name + '(%s)' % self.id

    def __str__(self):
        return repr(self)

    class Meta(object):
        abstract = True


class MyUser(AbstractUser):
    RELATIONSHIP_STATUSES = (
        ('y', '연애중'),
        ('n', '싱글'),
        ('m', '결혼'),
    )

    relationship_status = models.CharField(max_length=1, null=True, blank=True,
                                           choices=RELATIONSHIP_STATUSES)
    IMAGE_DIR = 'profile-images'
    profile_image = models.ImageField(
        upload_to=IMAGE_DIR, null=False,
        blank=True,
        default=settings.STATIC_URL+'images/default_profile.png')
    birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)


class Post(Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    IMAGE_DIR = 'post-images'
    image = models.ImageField(upload_to=IMAGE_DIR, null=True, blank=True)


class Comment(Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)


class Friend(Model):
    first_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    second_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    created = models.DateTimeField(auto_now_add=True)


class FriendRequest(Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    created = models.DateTimeField(auto_now_add=True)


class PostLike(Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)


class CommentLike(Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.ForeignKey(Comment)
