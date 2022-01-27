from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from polls.models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = Choice.objects.filter(question_id=question.id).order_by('choice_text')
    return render(request, 'polls/detail.html', {'question': question, 'choices': choices})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = Choice.objects.filter(question_id=question.id).order_by('-votes')
    return render(request, 'polls/results.html', {'question': question, 'choices': choices})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = Choice.objects.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        messages.error(request, "Você não selecionou uma opção.")
        return detail(request, question.id)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return results(request, question.id)
