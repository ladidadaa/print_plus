from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('logout/', logout_user, name='logout'),
    path('ajax_login/', ajax_login, name='ajax_login'),
    path('ajax_registr/', ajax_registr, name='ajax_registr'),
]
