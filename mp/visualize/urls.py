from django.urls import re_path, include
from .views import *

urlpatterns = [
    re_path(r'^get_bookmarks$', get_bookmarks),
    re_path(r'^remove_bookmark$', remove_bookmark),
    re_path(r'^add_bookmark$', add_bookmark),
    re_path(r'^get_sharing_groups$', get_sharing_groups),
    re_path(r'share_bookmark$', share_bookmark),
    re_path(r'^map', show_embedded_map),
    re_path(r'^mobile', show_mobile_map),
    re_path(r'', show_planner),
]
