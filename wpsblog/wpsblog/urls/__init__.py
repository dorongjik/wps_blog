from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from wpsblog.views import *



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^watcha/$', news, name="news"),
    url(r'^about/$', about, name="about"),

    url(r'^posts/', include("wpsblog.urls.posts", namespace="posts")),
    url(r'^policy/', include("wpsblog.urls.policy", namespace="policy")),
    url(r'^auth/', include("wpsblog.urls.auth", namespace="auth")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]