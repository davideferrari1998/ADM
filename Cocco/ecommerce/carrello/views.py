from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import ItemCarrello
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def carrelloDetails(request, user):
    items = ItemCarrello.objects.filter(utente=user)
    if len(items) > 0:
        return render(request, 'carrello/cart.html', {'items': items})
    else:
        return HttpResponse("Carrello vuoto")

@login_required
def checkout(request, user):
    ItemCarrello.objects.filter(utente=user).delete()
    return HttpResponse("Checkout")