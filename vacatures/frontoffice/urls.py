from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'frontoffice'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[a-zA-z0-9\-]+)/$', views.detail, name='detail'),
]
