#coding: utf-8
from django.conf.urls.defaults import patterns, url

from mods.views.add_module import addModule

urlpatterns = patterns('',
    #url(r'^deletelog/(?P<logId>\d+)/$', deleteLog),
    url(r'^add$', addModule),
)
