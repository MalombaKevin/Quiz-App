from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Answer, Question, Quiz, QuizTaker, UsersAnswer
from .serializers import MyQuizListSerializer, QuizDetailSerializer, QuizListSerializer, QuizResultSerializer, UsersAnswerSerializer


# Create your views here.
def index(request):
    return render('', 'index.html')

#Api views


class MyQuizListAPI(generics.ListAPIView):
	permission_classes = [
		permissions.IsAuthenticated
	]
	serializer_class = MyQuizListSerializer

	def get_queryset(self, *args, **kwargs):
		queryset = Quiz.objects.filter(quiztaker__user=self.request.user)
		query = self.request.GET.get("q")

		if query:
			queryset = queryset.filter(
				Q(name__icontains=query) |
				Q(description__icontains=query)
			).distinct()

		return queryset

        
class QuizListAPI(generics.ListAPIView):
	serializer_class = QuizListSerializer
	permission_classes = [
		permissions.IsAuthenticated
	]

	def get_queryset(self, *args, **kwargs):
		queryset = Quiz.objects.filter(roll_out=True).exclude(quiztaker__user=self.request.user)
		query = self.request.GET.get("q")

		if query:
			queryset = queryset.filter(
				Q(name__icontains=query) |
				Q(description__icontains=query)
			).distinct()

		return 