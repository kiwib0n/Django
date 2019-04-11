from django.db import models

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Group(models.Model):
    name = models.CharField(max_length=150)
    count_subscribes = models.IntegerField(default=0)
    descriptions = models.CharField(max_length=500)

