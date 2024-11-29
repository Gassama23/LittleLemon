from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import MenuItem  # Assurez-vous que le modèle MenuItem est bien défini
from .serializers import MenuItemSerializer  # Importez le sérialiseur que vous avez créé
from rest_framework import viewsets
from .models import Booking  # Importer le modèle Booking
from .serializers import BookingSerializer  # Importer le sérialiseur
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.permissions import AllowAny




# Create your views here.
def index(request):
    return render(request, 'index.html', {})


# Vue pour gérer la liste des éléments de menu et leur création (GET, POST)
class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]  
    queryset = Menu.objects.all()  # Récupérer tous les objets du modèle MenuItem
    serializer_class = MenuSerializer  # Utiliser le sérialiseur MenuItemSerializer

# Vue pour gérer un seul élément du menu (GET, PUT, DELETE)
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()  # Récupérer tous les objets du modèle MenuItem
    serializer_class = MenuItemSerializer  # Utiliser le sérialiseur MenuItemSerial



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Récupère tous les objets du modèle Booking
    serializer_class = BookingSerializer  # Utilise le sérialiseur BookingSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()  # Récupère tous les utilisateurs
    serializer_class = UserSerializer  # Sérialiseur pour les utilisateurs
    permission_classes = [permissions.IsAuthenticated]  # Seuls les utilisateurs authentifiés peuvent accéder