
from django.urls import path
from . import views as user_view
app_name = 'votingapp'

urlpatterns = [
    path('', user_view.home, name='home'),
    path('<int:question_id>/detail/', user_view.detail, name='detail'),
    path('<int:question_id>/result/', user_view.result, name='result'),
    path('<int:question_id>/vote/', user_view.vote, name='vote'),
]