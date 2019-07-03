from django.urls import re_path, path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve as static_serve

from django.conf import settings
from data_manager.api import LayerResource, ThemeResource, TocThemeResource
from tastypie.api import Api
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import visualize
import explore
#from mapproxy.views import proxy_view
from map_proxy.views import mapproxy_view
# print dir(map_proxy)
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(LayerResource())
v1_api.register(ThemeResource())
v1_api.register(TocThemeResource())


urlpatterns = [
                       path('', include('social.apps.django_app.urls', namespace='social')),
                       re_path(r'^api/', include(v1_api.urls)),
                       re_path(r'^mp_profile/', include('mp_profile.urls')),
                       #re_path(r'^sdc/', include('scenarios.urls')),
                       #re_path(r'^drawing/', include('drawing.urls')),
                       re_path(r'^data_manager/', include('data_manager.urls')),
                       #re_path(r'^learn/', include('learn.urls')),
                       #re_path(r'^scenario/', include('scenarios.urls')),
                       re_path(r'^explore/', include('explore.urls')),
                       re_path(r'^visualize/', include('visualize.urls')),
                       re_path(r'^planner/', include('visualize.urls')),
                       re_path(r'^embed/', include('visualize.urls')),
                       re_path(r'^mobile/', include('visualize.urls')),
                       re_path(r'^feedback/', include('feedback.urls')),
                       re_path(r'^proxy/', include('mp_proxy.urls')),
                       re_path(r'^mapproxy/(?P<path>.*)', mapproxy_view),
                       re_path(r'^([\w-]*)/planner/', visualize.views.show_planner),
                       re_path(r'^([\w-]*)/visualize/', visualize.views.show_planner),
                       re_path(r'^([\w-]*)/embed/',
                        visualize.views.show_embedded_map),
                       re_path(r'^([\w-]*)/catalog/', explore.views.data_catalog),
                       re_path(r'^$', RedirectView.as_view(url='/visualize')),
                       re_path(r'^media/admin/(?P<path>.*)$',
                               static_serve,
                               {"document_root": settings.ADMIN_MEDIA_PATH}),
                       re_path(r'', include('madrona.common.urls')),
            ]


if settings.DEBUG:
    # urlpatterns = [
    #     re_path("^media/admin/(?P<path>.*)$",
    #     static_serve,
    #     {"document_root": settings.ADMIN_MEDIA_PATH})) + urlpatterns

    urlpatterns += staticfiles_urlpatterns()
