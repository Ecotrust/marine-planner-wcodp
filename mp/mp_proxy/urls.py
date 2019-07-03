from django.urls import re_path, include
from .views import *

urlpatterns = [
    re_path(r'^get_legend_json/(?P<url>)$', getLegendJSON),
    re_path(r'^layer/(?P<layer_id>\d*)', layer_proxy_view),
    re_path('events/get_filters', get_filters),
    re_path(r'^capabilities/(?P<layer_id>\d*)', capabilities_proxy_view),
]
