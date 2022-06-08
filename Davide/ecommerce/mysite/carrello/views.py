from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Prodotto
from carrello.models import Carrello, CarrelloForm
from django.contrib.auth.decorators import login_required 

@login_required
def CartView(request, user):

    utente = request.user.id
    if utente == user:
        cart = Carrello.objects.filter(user=user)
        return render(request, 'carrello/cart.html', {'cart': cart})
    else:
        return HttpResponse("Accesso non consentito")


@login_required
def CartCheckout(request, user):
    
    utente = request.user.id
    if utente == user:
        Carrello.objects.filter(user = user).delete()
        return HttpResponse("Checkout effettuato!")
    else:
        return HttpResponse("Accesso non consentito")
        
