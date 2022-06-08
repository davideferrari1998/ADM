from django.urls import path
from django.contrib.auth.decorators import login_required 
from . import views

urlpatterns = [
    path('<tipo_lettura>', views.LetturaView),
    path('<tipo_lettura>/JSON', views.LetturaViewJSON),
    path('form/sensor', login_required(views.SensorFormView.as_view())),
    path('form/sensor/<int:pk>/modify', login_required(views.SensorFormModify.as_view())),
    path('form/sensor/<int:pk>/delete', login_required(views.SensorFormDelete.as_view())),
    path('', views.index, name='index')
]