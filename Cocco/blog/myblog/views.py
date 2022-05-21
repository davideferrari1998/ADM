
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Articoli, ArticoliForm
from django.contrib.auth.decorators import login_required 

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

@login_required
def ArticoliFormView(request):

    if request.method == 'POST':

        form = ArticoliForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponse('Articolo inserito')
        else:
            return HttpResponse('form not valid')

    else:
        form = ArticoliForm()
        form.fields['pub_date'].initial = datetime.now()
        return render(request, 'myblog/form.html', {'form':form})