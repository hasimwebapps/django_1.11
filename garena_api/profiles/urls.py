# coding: utf8
import django

try:
    from django.conf.urls.defaults import url
except:
    from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import show

urlpatterns = [

    url(r'ping', show),

]
