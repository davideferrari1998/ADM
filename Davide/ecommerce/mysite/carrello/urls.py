from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required 

urlpatterns = [
    path('<int:user>', views.CartView),
    path('<int:user>/checkout', views.CartCheckout)
]