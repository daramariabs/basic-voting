from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_quetion_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_quetion_list': latest_quetion_list
    }
    
    return render(request, 'polls/index.html', context)

def detail(request, quetion_id):
    question = Question.objects.get(Question, pk=quetion_id)
    return render(request, 'pools/detail.html', {'question':question})

def results(request, quetion_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % quetion_id)

def vote(request, quetion_id):
    return HttpResponse("You're voting on question %s" % quetion_id)
