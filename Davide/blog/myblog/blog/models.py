from dataclasses import fields
from datetime import datetime
from turtle import title
from typing import Text
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

    def __str__(self):
        return str(self.nickname)
    

class Articolo(models.Model):
    autore = models.ForeignKey(Autore, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return str(self.title)

    def valid_date(self):
        now = timezone.now()
        return self.pub_date <= now 

    class Meta:
        ordering = ['pub_date'] #-pub  per cambiare ordine



# Forms

class ArticoliForm(ModelForm):
    class Meta:
        model = Articolo
        fields = '__all__'



    
    