from django.shortcuts import (
    render, get_object_or_404,
    HttpResponseRedirect, reverse, redirect)
from . models import Question, Choice
from .forms import QuestionForm
from django.contrib import messages
from django.views.generic import CreateView

def home(request):
    latest_question_list = Question.objects.order_by('-pub_date')
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
    return HttpResponseRedirect(reverse('votingapp:result', args=(question.id,)))

# def poll_question(request):
#     if request.method == 'POST':
#         q_form = QuestionForm(request.POST)
#         if q_form.is_valid():
#             q_form.save()
#             messages.success(request, f'New Question added')
#         return redirect('votingapp:home')
#     else:
#        q_form = QuestionForm()
#        return render(request, 'votingapp/poll_questions.html', {'q_form': q_form})

class QuestionCreateView(CreateView):
    model = Question
    fields = ['question_text']
    template_name = 'votingapp/poll_questions.html'

class ChoiceCreateView(CreateView):
    model = Choice
    fields = '__all__'
    template_name = 'votingapp/poll_choice.html'

# deleting a question will automatically delete it's choices (models.CASCADE)
def delete(request, question_id):
    item = Question.objects.get(id=question_id).delete()
    messages.success(request, 'question deleted')
    return redirect('votingapp:home')

def delete_choice(request, choice_id):
    item = Choice.objects.get(id=choice_id).delete()
    messages.success(request, 'choice deleted')
    return redirect('votingapp:home')

def edit(request, question_id):
        if request.method == 'POST':
            employee = Question.objects.get(pk=question_id)
            form = QuestionForm(request.POST or None, instance=employee)
            if form.is_valid():
                form.save()
                messages.success(request, f'question edited')
            return redirect('votingapp:home')
        else:
            employee = Question.objects.get(pk=question_id)
        return render(request, 'votingapp/edit_question.html', {'employee': employee})