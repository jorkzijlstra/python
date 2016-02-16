from django.conf.urls import url, include
from django.contrib import admin
from . import actions

urlpatterns = [
    url(r'^publish/(?P<slug>[a-zA-z0-9]+)/$', actions.publish, name='publish'),
    url(r'^', admin.site.urls),
]
