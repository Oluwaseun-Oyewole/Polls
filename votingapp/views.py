from django.shortcuts import (
    render, get_object_or_404,
    HttpResponseRedirect, reverse)
from . models import Question, Choice


def home(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'votingapp/home.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'votingapp/detail.html', {'question': question})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'votingapp/result.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'votingapp/detail.html', {
            'question': question,
            'error_message': 'You did not select any choice'
        })
    else:
        choice.votes+=1
        choice.save()
    # return render(request, 'votingapp/result.html', {'question': question})
    return HttpResponseRedirect(reverse('votingapp:result', args=(question.id,)))
