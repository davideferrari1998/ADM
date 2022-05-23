from django import views
from django.urls import path
from .views import carrelloDetails, checkout

urlpatterns = [
    path('<int:user>/', carrelloDetails), #lista prodotti
    path('<int:user>/checkout/', checkout)
]