from django.db import models
from django.contrib.auth.models import User

from prodotto.models import Prodotto

# Create your models here.
class ItemCarrello(models.Model):
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    prodotti = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
