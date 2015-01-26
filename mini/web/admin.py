from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.MyUser)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Friend)
admin.site.register(models.FriendRequest)
admin.site.register(models.PostLike)
admin.site.register(models.CommentLike)
