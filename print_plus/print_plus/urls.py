from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from print_plus import settings
from photo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')),
]
