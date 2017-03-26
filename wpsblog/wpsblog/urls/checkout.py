from django.conf.urls import url
from wpsblog.views import *

urlpatterns = [
    url(r'^step1/$', step1, name="step1"),
    url(r'^step2/$', step2, name="step2"),
]