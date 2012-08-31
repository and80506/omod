#coding: utf-8
from django.conf.urls.defaults import patterns, url

from mods.views.insert_data import insertData
from mods.views.get_mod import getMod
from mods.views.get_type import getType

urlpatterns = patterns('',
    url(r'^insert_data$', insertData),
    url(r'^get_type$', getType),
    url(r'^get_mod$', getMod)
)
