from django.db import models
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm

from prodotto.models import Prodotto

# Create your models here.
class ItemCarrello(models.Model):
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    prodotti = models.ForeignKey(Prodotto, on_delete=models.CASCADE)

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=False)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user