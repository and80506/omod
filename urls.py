from django.conf.urls.defaults import patterns, include, url
<<<<<<< HEAD
from django.conf import settings

urlpatterns = patterns('',
    url(r'^omod/', include("mods.urls")),
     #static files
    url(r'^omod/media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
=======

urlpatterns = patterns('',
    url(r'^omod/', include("mods.urls")),
>>>>>>> 92f07fa2e1a329acd9701faaf566aad83950eb55
)
