from django.conf.urls import url
# from django.contrib import admin
# from posts.views import post_home
# from posts import views
from . import views

urlpatterns = [
    # url(r'^posts/$', views.post_home),
    # url(r'^$', post_home),
    url(r'^$', views.post_list),
    url(r'^create/$', views.post_create),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
    url(r'^update/$', views.post_update),
    url(r'^delete/$', views.post_delete),
    
]