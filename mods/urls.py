#coding: utf-8
from django.conf.urls.defaults import patterns, url

from mods.views.add_module import addModule
from mods.views.update_module import updateModule
from mods.views.update_module_result import updateModuleResult
from mods.views.add_type import addType
from mods.views.get_type import getType
from mods.views.get_mod import getMod
from mods.views.add_module_result import addModuleResult
from mods.views.insert_data import insertData

urlpatterns = patterns('',
    #url(r'^deletelog/(?P<logId>\d+)/$', deleteLog),
    url(r'^add_mod$', addModule),
    url(r'^update_mod/(?P<update_mod_id>\d+)/$', updateModule),
    url(r'^addModuleResult', addModuleResult),
    url(r'^updateModuleResult', updateModuleResult),
    url(r'^add_type$', addType),
    url(r'^get_type$', getType),
    url(r'^get_mod$', getMod),
    url(r'^insert_data', insertData),
)

