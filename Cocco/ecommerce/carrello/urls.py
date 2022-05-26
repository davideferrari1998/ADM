from django import views
from django.urls import path
from .views import carrelloDetails, checkout

app_name = "cart"

urlpatterns = [
    path('<int:user>/', carrelloDetails, name="carrelloDet"), #lista prodotti
    path('<int:user>/checkout/', checkout)
]