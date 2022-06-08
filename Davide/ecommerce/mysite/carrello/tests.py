from django.test import TestCase
from .models import Prodotto
from carrello.models import Carrello, CarrelloForm

# Create your tests here.

def test_quantity_minor_zero(self):
      
        x = CarrelloForm({'name':'prova', 'price':15, 'quantity': 0})
        self.assertIs(x.validate_quantity(), False)