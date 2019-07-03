from django.urls import re_path, include
from .views import *

urlpatterns = [
    re_path(r'^send', send_feedback),
    # (r'^bookmark', send_bookmark),
]
