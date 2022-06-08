from django.urls import path

from . import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<int:user>/posts/<int:year>/<int:month>', views.PostsView.as_view()),
    path('<int:user>/posts/<int:year>/<int:month>/<int:pk>', views.PostsDetail.as_view()),
    path('form', views.ArticoliFormView),
    path('form/<int:pk>/delete', login_required(views.ArticoliFormDelete.as_view())),
    path('form/<int:pk>/modify', login_required(views.ArticoliFormModify.as_view()))
]