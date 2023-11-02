
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ETAdom/', include('ETAdom.urls')),
    path('common/', include('common.urls')),
]
