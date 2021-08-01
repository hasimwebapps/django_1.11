# coding: utf8
from django.conf.urls import url

from .views import user_list, user_add, user_login

urlpatterns = [

    url(r'list', user_list),
    url(r'add', user_add),
    url(r'login', user_login),

]
