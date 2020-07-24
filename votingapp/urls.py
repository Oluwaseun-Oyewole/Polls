
from django.urls import path
from . import views as user_view
app_name = 'votingapp'

urlpatterns = [
    path('', user_view.home, name='home'),
    path('<int:question_id>/detail/', user_view.detail, name='detail'),
    path('<int:question_id>/result/', user_view.result, name='result'),
    path('<int:question_id>/vote/', user_view.vote, name='vote'),
    # path('poll_question/', user_view.poll_question, name='poll_question'),
    path('poll_question/', user_view.QuestionCreateView.as_view(), name='poll_question'),
    path('poll_choice/', user_view.ChoiceCreateView.as_view(), name='poll_choice'),
    path('<int:question_id>/delete/', user_view.delete, name='delete'),
    path('<int:choice_id>/delete_choice/', user_view.delete_choice, name='delete_choice'),
    path('edit/<int:question_id>/', user_view.edit, name='edit'),

]