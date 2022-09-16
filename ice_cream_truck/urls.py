"""ice_cream_truck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from inventory.views import IceCreamModelViewset, ShavedIceModelViewset, SnackBarModelViewset, BuyFoodAPIView, TotalPriceAPIView

router = DefaultRouter()

router.register('api/ice-creams', IceCreamModelViewset, basename="ice_creams")
router.register('api/shaved-ice', ShavedIceModelViewset, basename="shaved_ice")
router.register('api/snackbars', SnackBarModelViewset, basename="snackbars")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/buy-food', BuyFoodAPIView.as_view(), name="buy_food"),
    path('api/inventory', TotalPriceAPIView.as_view(), name="inventory"),
]
