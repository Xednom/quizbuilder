from django.db import models
from django.utils import timezone


# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=250)
    date_created = models.DateTimeField('date published')
    expiration = models.DateTimeField('date of expiration')

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    question_text = models.TextField()
    date_created = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice_text = models.CharField(max_length=250)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
