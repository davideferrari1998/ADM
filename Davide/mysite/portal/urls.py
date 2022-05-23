from importlib.resources import path
from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
    # ex: /portal/
    path('', views.portal_welcome, name='portal_welcome'),
    path('logout/', views.logout_view, name='logout_view'),
]