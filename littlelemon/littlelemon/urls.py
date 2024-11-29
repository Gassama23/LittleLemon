"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from restaurant.views import BookingViewSet, UserViewSet  # Import direct des vues nécessaires
from rest_framework.authtoken.views import obtain_auth_token

# Créez un routeur pour gérer les routes API
router = DefaultRouter()
router.register(r'tables', BookingViewSet, basename='booking')  # Gestion des réservations
router.register(r'users', UserViewSet, basename='user')  # Gestion des utilisateurs

# Définition des URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),  # Routes spécifiques à l'application restaurant
    path('restaurant/booking/', include(router.urls)),  # API de réservation
    path('auth/', include('djoser.urls')),  # Authentification avec Djoser
    path('auth/', include('djoser.urls.authtoken')),  # Gestion des tokens
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Interface API DRF
    path('api-token-auth/', obtain_auth_token),  # Route pour obtenir un token d'authentification
]

