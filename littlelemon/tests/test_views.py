from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User  
from rest_framework.authtoken.models import Token


class MenuViewTest(TestCase):
    def setUp(self):
        # Ajouter des instances de test au modèle Menu
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)

        # Créer un utilisateur de test
        self.user = User.objects.create_user(username="admin", password="lemon@786!")

        # Créer un jeton pour l'utilisateur
        self.token = Token.objects.create(user=self.user)

        # Créer un client API pour envoyer des requêtes HTTP
        self.client = APIClient()

        # Ajouter le jeton à l'en-tête Authorization
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_getall(self):
        # Effectuer une requête GET à l'URL correspondante
        response = self.client.get('/restaurant/menu/')

        # Vérifier que la réponse est correcte
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Récupérer et sérialiser les objets Menu
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Vérifier que les données sérialisées correspondent à la réponse de l'API
        self.assertEqual(response.data, serializer.data)
