from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        # Créer une instance du modèle Menu
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        # Vérifier si la méthode __str__ renvoie la bonne chaîne
        self.assertEqual(str(item), "IceCream : 80")
