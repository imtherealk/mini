from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models import Q


class Model(models.Model):
    def __str__(self):
        return str(self.id)

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

    def is_friend_of(self, user):
        friendships = Friend.objects.filter(Q(first_user=self) | Q(second_user=self))
        return friendships.filter(Q(first_user=user) | Q(second_user=user)).exists()

    def sent_request_to(self, user):
        return FriendRequest.objects.filter(from_user=self, to_user=user).exists()


class Post(Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    IMAGE_DIR = 'post-images'
    image = models.ImageField(upload_to=IMAGE_DIR, null=True, blank=True)
    likes = models.IntegerField(default=0)


class Comment(Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
    likes = models.IntegerField(default=0)


class Friend(Model):
    first_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    second_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    created = models.DateTimeField(auto_now_add=True)


class FriendRequest(Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    accepted = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


class PostLike(Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)


class CommentLike(Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.ForeignKey(Comment)
