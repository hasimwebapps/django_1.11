from django.conf.urls import include, url
from django.contrib import admin
# from django.urls import path
# from profiles import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mywebsite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^profiles/', views.views, name='profiles'),
    url(r'^api/tools/', include('profiles.urls')),


]
