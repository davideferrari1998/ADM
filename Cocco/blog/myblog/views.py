
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Articoli, Autore
import datetime

# Create your views here.
class PostsView(generic.ListView):
    context_object_name = 'posts_month'
    template_name = 'myblog/posts.html'

    def get_queryset(self):
        autore_id = self.kwargs["user"]
        year = self.kwargs["year"]
        month = self.kwargs["month"]
        posts = Articoli.objects.filter(pub_date__month=month, pub_date__year=year, autore = autore_id)
        return posts

def PostsDetail(request, user, year, month, post_id):
    context_object_name = 'post_detail'
    template_name = 'myblog/detail.html'

    post = get_object_or_404(Articoli, autore = user, pub_date__month=month, pub_date__year=year, pk = post_id)
    return render(request, template_name, {context_object_name: post})