from django.urls import path
from .views import letturaView, letturaViewJson, sensoriJquery, manageRilevamentiForm

app_name = 'climate_monitor'

urlpatterns = [
    path('<str:tipo_lettura>', letturaView),
    path('<str:tipo_lettura>/json', letturaViewJson, name="reqjson"),
    path('jq', sensoriJquery, name="jq"),
    path('form', manageRilevamentiForm)
]