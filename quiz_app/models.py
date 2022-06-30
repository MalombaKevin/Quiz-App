from django.db import models
from django.conf import settings

# Create your models here.

class Quiz(models.Model):
	name = models.CharField(max_length=100)

class QuizTaker(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	completed = models.BooleanField(default=False)
	date_finished = models.DateTimeField(null=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.email