
from django.conf.urls import url
from django.contrib import admin
from .views import posts_create,posts_detail,posts_update,posts_delete,posts_list

urlpatterns = [
    url(r'^create/$', posts_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', posts_detail, name = 'detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', posts_update, name = 'update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', posts_delete),
    url(r'^$', posts_list, name='list'),
]
