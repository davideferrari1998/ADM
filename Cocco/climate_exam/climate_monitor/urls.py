from django import views
from django.urls import path
from .views import letturaView, letturaViewJson, sensoriJquery, manageRilevamentiForm, SensorFormView, RilevamentoFormModify, updateRilevamentiForm

app_name = 'climate_monitor'

urlpatterns = [
    path('<str:tipo_lettura>', letturaView),
    path('<str:tipo_lettura>/json', letturaViewJson, name="reqjson"),
    path('form/', manageRilevamentiForm),
    path('form/rilevamenti', SensorFormView.as_view()),
    path('form/sensor/<int:pk>/modify', RilevamentoFormModify.as_view()),
    path('update/<int:pk>', updateRilevamentiForm)
]