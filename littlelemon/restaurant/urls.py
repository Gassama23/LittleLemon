from django.urls import path
from .views import MenuItemView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', MenuItemView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-retrieve-update-destroy'),

]
