from django.urls import path
from prodotto import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='prod_list'), #lista prodotti
    path('<int:prod_id>/', views.ProductDetailView), #dettaglio prodotto
    path('<int:prod_id>/buy/', views.PurchaseProductView), #acquista prodotto
]