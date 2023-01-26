from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("bucket/", bucket, name="bucket"),
    path("logout/", logout_user, name="logout"),
    path("ajax_login/", ajax_login, name="ajax_login"),
    path("ajax_registr/", ajax_registr, name="ajax_registr"),
    path("ajax_doctype/", ajax_doctype, name="ajax_doctype"),
    path("ajax_order/", ajax_order, name="ajax_order"),
    path("ajax_uploadFile/", ajax_uploadFile, name="ajax_uploadFile"),
    path("ajax_uploadOrder/", ajax_uploadOrder, name="ajax_uploadOrder"),
]
