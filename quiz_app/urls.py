
from unicodedata import name
from django.urls import path,re_path
from  .views import *
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', index, name='index'),
    path("my-quizzes/", MyQuizListAPI.as_view(),name='my_quizlist'),
	path("quizzes/", QuizListAPI.as_view(), name='quizzes'),
	path("save-answer/", SaveUsersAnswer.as_view(),name='save_answer'),
	re_path(r"quizzes/(?P<slug>[\w\-]+)/$", QuizDetailAPI.as_view(), name='quizdetail'),
	re_path(r"quizzes/(?P<slug>[\w\-]+)/submit/$", SubmitQuizAPI.as_view(),name='submit'),
	path('taker',TakerApi.as_view(),name='quiztaker'),
	path('docs/',include_docs_urls(title='Quiz Brainer Api'),name='endpoints'),
	path('schema',
	get_schema_view(
	title="Quiz Brainer Api",
	description='an api for quiz blog',
	version='1.0.0'
	),
	name='openschema'
	
	  
	  
	  )
]
