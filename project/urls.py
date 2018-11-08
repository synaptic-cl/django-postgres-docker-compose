"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers

from main.views import ProductViewset, FamilyViewset, LocationViewset


router = routers.DefaultRouter()
router.register(r'products', ProductViewset)
router.register(r'families', FamilyViewset)
router.register(r'location', LocationViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.STATIC_URL+'admin/css/',
        document_root=settings.STATIC_ROOT)
