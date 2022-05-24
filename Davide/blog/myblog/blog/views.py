from datetime import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views import generic

import blog
from .models import Autore, Articolo, ArticoliForm
from django.contrib.auth.decorators import login_required 

# Create your views here.
class PostsView(generic.ListView):
    context_object_name = 'posts_month'
    template_name = 'blog/posts.html'

    def get_queryset(self):
        autore_id = self.kwargs["user"]
        year = self.kwargs["year"]
        month = self.kwargs["month"]
        posts = Articolo.objects.filter(pub_date__month=month, pub_date__year=year, autore = autore_id)
        return posts

"""
def PostsDetail(request, user, year, month, post_id):
    context_object_name = 'post_detail'
    template_name = 'blog/detail.html'

    post = get_object_or_404(Articolo, autore = user, pub_date__month=month, pub_date__year=year, pk = post_id)
    return render(request, template_name, {context_object_name: post})
"""

class PostsDetail(generic.DetailView):
    model = Articolo
    template_name = 'blog/detail.html'
    context_object_name = 'post_detail'

    def get_queryset(self):
        autore_id = self.kwargs["user"]
        year = self.kwargs["year"]
        month = self.kwargs["month"]
        post_id = self.kwargs["pk"]
        return Articolo.objects.filter(pub_date__month=month, pub_date__year=year, autore = autore_id, pk = post_id)
     

@login_required
def ArticoliFormView(request):

    if request.method == 'POST':

        form = ArticoliForm(request.POST)
        
        if form.is_valid() and form.instance.valid_date():
            form.save()
            return HttpResponse('Articolo inserito')
        else:
            return HttpResponse('Form non valido')

    else:
        form = ArticoliForm()
        form.fields['pub_date'].initial = datetime.now()
        return render(request, 'blog/form.html', {'form':form})


class ArticoliFormModify(generic.edit.UpdateView):
    model = Articolo
    template_name = 'blog/form.html'
    fields = ['title', 'text', 'pub_date']
    
    success_url = '/'

"""
@login_required
def ArticoliFormModify(request, id):

    try:
        art = get_object_or_404(Articolo, pk = id)
    except Http404:
        return HttpResponse("Articolo non esistente")

    if request.method == 'POST':

        form = ArticoliForm(request.POST, instance= art)
        
        if form.is_valid() and form.instance.valid_date():
            form.save()
            return HttpResponse('Articolo Modificato')
        else:
            return HttpResponse('Form non valido')

    else:
        form = ArticoliForm(data= {'autore':art.autore, 'title': art.title, 'text': art.text, 'pub_date': art.pub_date})
        return render(request, 'blog/form.html', {'form':form})

"""

class ArticoliFormDelete(generic.edit.DeleteView):
    model = Articolo
    success_url = '/'

