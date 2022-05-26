from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.decorators import login_required

from prodotto.models import Prodotto
from carrello.models import ItemCarrello

# Create your views here.
class ProductListView(generic.ListView):
    template_name = 'prodotto/listaprodotti.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Prodotto.objects.all()

def ProductDetailView(request, prod_id):
    prodotto = get_object_or_404(Prodotto, pk=prod_id)
    return render(request, 'prodotto/productdetails.html',{'prodotto': prodotto})
    
  
@login_required
def PurchaseProductView(request, prod_id):
    user = request.user
    if user.is_authenticated:
        try:
            prodotto = get_object_or_404(Prodotto, pk=prod_id)
        except Http404:
            return HttpResponse("Prodotto non trovato")
        ItemCarrello.objects.create(utente=user, prodotti=prodotto)
        return HttpResponseRedirect(reverse('prod_list'))
    else:
        return HttpResponse("necessario login per aggiungere item al carrello")