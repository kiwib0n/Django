from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Question, Group
from django.template import RequestContext, loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    template = loader.get_template("polls/index.html")

    context = {'latest_question_list': latest_question_list,}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Вопрос не существует")
    return render(request, 'polls/detail.html', {'question':question})

def result(request, question_id):
    response = "Вы посмотрели результат вопроса. %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Вы ответили на этот вопрос %s." % question_id)
