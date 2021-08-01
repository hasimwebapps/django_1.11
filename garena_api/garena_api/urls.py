from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'garena_api.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^profiles/', views.views, name='profiles'),
    url(r'^api/users/', include('profiles.urls')),


]
