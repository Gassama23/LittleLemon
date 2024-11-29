from rest_framework import serializers
from .models import MenuItem 
from .models import Menu 
from .models import Booking  
from django.contrib.auth.models import User
from rest_framework import serializers

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem  # Modèle sur lequel ce sérialiseur est basé
        fields = '__all__'  # Cela inclut tous les champs du modèle MenuItem


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Le modèle lié
        fields = '__all__'  # Inclut tous les champs du modèle Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  # Modèle sur lequel ce sérialiseur est basé
        fields = '__all__'  # Cela inclut tous les champs du modèle MenuItem
