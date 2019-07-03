from django.urls import re_path, include
from .views import *

urlpatterns = [
    re_path(r'^catalog', data_catalog),
    re_path(r'^needs', data_needs),
    re_path(r'^map_tile_example/([\w-]*)', map_tile_example),
    re_path(r'^map_tile_esri_example/([\w-]*)', map_tile_esri_example),
    re_path(r'^map_tile_leaflet_example/([\w-]*)', map_tile_leaflet_example),
    re_path(r'^arcrest_example/([\w-]*)', arcrest_example),
    re_path(r'^([\w-]*)', tiles_page)
]
