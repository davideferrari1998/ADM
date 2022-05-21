from django.urls import path
from . import views

urlpatterns = [
    path('<int:user>/posts/<int:year>/<int:month>', views.PostsView.as_view()),
    path('<int:user>/posts/<int:year>/<int:month>/<int:post_id>', views.PostsDetail),
]