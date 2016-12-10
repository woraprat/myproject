from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
@python_2_unicode_compatible
class Usb(models.Model):
    name = models.CharField(max_length=200)
    readspeed = models.FloatField(default=0)
    price = models.FloatField(default=0)

    def __str__(self):
        return '%c,%f,%f' % (self.name, self.readspeed,self.price)