from unicodedata import name
from django.urls import path,re_path
from  .views import *

urlpatterns = [
    path('', index, name='index'),
    path("my-quizzes/", MyQuizListAPI.as_view(),name='my_quizlist'),
	path("quizzes/", QuizListAPI.as_view(), name='quizzes'),
	path("save-answer/", SaveUsersAnswer.as_view(),name='save_answer'),
	re_path(r"quizzes/(?P<slug>[\w\-]+)/$", QuizDetailAPI.as_view(), name='quizdetail'),
	re_path(r"quizzes/(?P<slug>[\w\-]+)/submit/$", SubmitQuizAPI.as_view(),name='submit'),
]
