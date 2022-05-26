from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .models import ItemCarrello
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def carrelloDetails(request, user):
    if request.user.id == user:
        items = ItemCarrello.objects.filter(utente=user)
        if len(items) > 0:
            return render(request, 'carrello/cart.html', {'items': items})
        else:
            return HttpResponse("Carrello vuoto")
    else:
        return HttpResponse("Stai provando ad accedere ad un carrello non in tuo possesso")

@login_required
def checkout(request, user):
    if request.user.id == user:
        ItemCarrello.objects.filter(utente=user).delete()
        return HttpResponse("Checkout")
    else:
        return HttpResponse("Accesso non consentito")