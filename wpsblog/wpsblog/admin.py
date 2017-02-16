from django.contrib import admin

from wpsblog.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)