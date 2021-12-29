from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Choice, Question
from django.urls import reverse

def index(request):
    latest_quetion_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_quetion_list': latest_quetion_list
    }
    
    return render(request, 'polls/index.html', context)

def detail(request, quetion_id):
    question = get_object_or_404(Question, pk=quetion_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, quetion_id):
    question = get_object_or_404(Question, pk=quetion_id)
    return render(request, 'polls/results.html', {'question':question})
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % quetion_id)

def vote(request, quetion_id):
    question = get_object_or_404(Question, pk=quetion_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
