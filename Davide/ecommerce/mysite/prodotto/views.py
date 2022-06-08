from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Prodotto
from carrello.models import Carrello
from django.contrib.auth.decorators import login_required 


# Create your views here.


class ProductsView(generic.ListView):

    context_object_name = 'products_list'
    template_name = 'prodotto/products_list.html'

    def get_queryset(self):
        return Prodotto.objects.all()

"""
class ProductDetailView(generic.DetailView):
    model = Prodotto
    template_name = 'prodotto/product_detail.html'
    context_object_name = 'prodotto'

    def get_queryset(self):
        prod_id = self.kwargs["pk"]
        return Prodotto.objects.filter(pk = prod_id)
"""

def ProductDetailView(request, prod_id):
    prodotto = get_object_or_404(Prodotto, pk=prod_id)
    return render(request, 'prodotto/product_detail.html',{'prodotto': prodotto})


@login_required
def ProductBuyView(request, prod_id):
    
    utente = request.user
    prodotto = get_object_or_404(Prodotto, pk=prod_id)
    Carrello.objects.create(user=utente, products = prodotto)
    #return HttpResponseRedirect(reverse('lista_prodotti'))
    return HttpResponse("Prodotto aggiunto con successo!")
    

"""
def ProductBuyView(request, prod_id):
    
    utente = request.user
    if utente.is_authenticated():
        Carrello.objects.create(user=utente, products=prod_id)
        #return HttpResponseRedirect(reverse('lista_prodotti'))
        return HttpResponse("Prodotto aggiunto con successo!")
    else:
        return HttpResponse("Necessario login per aggiungere prodotti al carrello!")
"""
    