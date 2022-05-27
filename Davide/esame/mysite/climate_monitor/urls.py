from django.urls import path

from . import views

urlpatterns = [
    path('<tipo_lettura>/', views.LetturaView),
    path('', views.index, name='index'),
]