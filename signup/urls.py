from django.urls import path
from signup.views import registration,signup
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url(r'^registration/$', registration),
    url(r'signup',signup,name='signup')
]