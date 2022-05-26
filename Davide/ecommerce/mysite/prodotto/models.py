from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class Prodotto(models.Model):

    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return str(self.name)