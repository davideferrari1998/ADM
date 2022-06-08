from django.urls import path
from .views import letturaView, letturaViewJson

app_name = 'climate_monitor'

urlpatterns = [
    path('<str:tipo_lettura>', letturaView),
    path('<str:tipo_lettura>/json', letturaViewJson),
]