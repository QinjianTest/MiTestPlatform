# MiTestPlatform/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/example/', permanent=False)),
    path('', include('core.urls')),  # 包含 core 应用的路由
]
