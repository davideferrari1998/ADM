from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

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
    
  

def PurchaseProductView(request, prod_id):
    user = request.user
    if user.is_authenticated():
        ItemCarrello.objects.create(utente=user, prodotti=prod_id)
        return HttpResponseRedirect(reverse('prod_list'))
    else:
        return HttpResponse("necessario login per aggiungere item al carrello")