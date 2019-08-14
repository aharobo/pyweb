
from django.contrib import admin
from django.urls import path, include

from booktest.views import *

urlpatterns = [
    path('', include("web.urls")),
    path('admin/', admin.site.urls),
    path('book/', include("booktest.urls"))
]
