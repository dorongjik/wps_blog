from django.conf.urls import url
from wpsblog.views import *

urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^signup/$', signup, name="signup"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^mypage/$', mypage, name="mypage"),
    url(r'^mypage/profile$', profile, name="profile"),
    url(r'^mypage/update_profile$', update_profile, name="update_profile"),
    
]