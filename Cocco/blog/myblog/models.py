from dataclasses import fields
from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.forms import DateTimeInput, ModelForm
from django.forms import widgets

# Create your models here.
class Autore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nickname

class Articoli(models.Model):
    autore = models.ForeignKey(Autore, on_delete=models.CASCADE)
    titolo = models.CharField(max_length=30)
    testo = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    class Meta:
        ordering = ['pub_date']

    def __str__(self) -> str:
        return self.titolo

    def valid_date(self):
        now = timezone.now()
        return self.pub_date <= now 

# Forms

class ArticoliForm(ModelForm):
    class Meta:
        model = Articoli
        fields = '__all__'

