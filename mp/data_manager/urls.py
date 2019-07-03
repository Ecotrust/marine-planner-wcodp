# from django.conf.urls import url, include
from django.urls import re_path, include
from .views import *

urlpatterns = [
    re_path(r'^layer/([A-Za-z0-9_-]+)$', update_layer),
    re_path(r'^layer', create_layer),
    re_path(r'^wa_config', load_config),
    re_path(r'^get_json/([\w-]*)', get_json),
    re_path(r'^geoportal_ids', geoportal_ids)
]
