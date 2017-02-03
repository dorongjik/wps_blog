from django.conf.urls import url, include
from django.contrib import admin
from wpsblog.views import *
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^watcha/$', news, name="news"),
    url(r'^about/$', about, name="about"),
    
    url(r'^posts/$', lists, name="posts-lists"),
    url(r'^posts/(?P<post_id>\d+)/$', detail, name="posts-room"),

    url(r'^policy/', include("wpsblog.urls.policy", namespace="policy")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]