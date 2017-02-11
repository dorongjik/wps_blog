from django.conf.urls import url
from wpsblog.views.posts import *

urlpatterns = [
    url(r'^$', lists, name="lists"),
    url(r'^(?P<post_id>\d+)/$', detail, name="detail"),
    url(r'^new/$', new, name="new"),
    url(r'^create/$', create, name="create"),
    url(r'^(?P<post_id>\d+)/edit/$', edit, name="edit"),
    url(r'^(?P<post_id>\d+)/update/$', update, name="update"),
    url(r'^(?P<post_id>\d+)/delete/$', delete, name="delete"),

    url(r'^(?P<post_id>\d+)/comments/create/$', create_comment, name="create-comment"),
    url(r'^(?P<post_id>\d+)/comments/(?P<comment_id>\d+)/delete$', delete_comment, name="delete-comment"),

]