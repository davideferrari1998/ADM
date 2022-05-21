from django.db import models
from django.contrib import admin

# Create your models here.
class Autore(models.Model):
    nickname = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nickname

class Articoli(models.Model):
    autore = models.ForeignKey(Autore, on_delete=models.CASCADE)
    titolo = models.CharField(max_length=30)
    testo = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    class Meta():
        ordering = ['pub_date']

    def __str__(self) -> str:
        return self.titolo