import datetime
from django.db import models
from datetime import date
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(verbose_name='Texto da questão', max_length=200)
    pub_date = models.DateField(verbose_name='Data', default=date.today)
    pub_time = models.TimeField(verbose_name='Hora', default=datetime.datetime.now().time)


    def was_published_recently(self):
        return self.pub_date >= date.today() - datetime.timedelta(days=1)


    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(verbose_name='Texto de escolha', max_length=200)
    votes = models.IntegerField(verbose_name='Votos', default=0)


    def __str__(self):
        return self.choice_text
