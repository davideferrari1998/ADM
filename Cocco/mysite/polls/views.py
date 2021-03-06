from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

# Create your views here.
# To call the view, we need to map it to a URL - and for this we need a URLconf
# To create a URLconf in the polls directory, create a file called urls.py.

'''
Each view is responsible for doing one of two things: returning an HttpResponse object
containing the content for the requested page, or raising an exception such as Http404
'''

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from .models import Question, Choice
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    #login_required = True

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    #login_required = True

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    #login_required = True

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))