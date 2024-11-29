from django.contrib import admin
from .models import Menu, Booking  # Importer les modèles

# Register your models here.
# Enregistrer les modèles dans l'admin

admin.site.register(Menu)
admin.site.register(Booking)
