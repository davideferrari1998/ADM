from django.db import models
from django.contrib.auth.models import User
from prodotto.models import Prodotto
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.

class Carrello(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Prodotto, on_delete=models.CASCADE)


class CarrelloForm(forms.Form):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    
    def validate_quantity(self):
        if self.quantity <= 0:
            return False
        else:
            return True
