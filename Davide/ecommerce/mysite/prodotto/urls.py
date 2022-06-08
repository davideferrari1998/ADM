from django.urls import path

from . import views

urlpatterns = [

    path('', views.ProductsView.as_view(), name='lista_prodotti'),
    path('<int:prod_id>', views.ProductDetailView),
    path('<int:prod_id>/buy', views.ProductBuyView)
]