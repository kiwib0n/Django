from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Question, Group, Choice
from django.template import RequestContext, loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    #template = loader.get.emplate("polls/index.html")

    context = {'latest_question_list': latest_question_list,}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Вопрос не существует")
    return render(request, 'polls/detail.html', {'question': question})

def result(request, doct):
    response = "Вы посмотрели результат вопроса. "+str(doct)
    return HttpResponse(response)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'Ты не выбрал ответ',
        })
    else:

        selected_choice.votes += 1
        selected_choice.save()

        doct = {'question':question, 'voice': selected_choice}

        return render(request, 'polls/{}/results/', doct )