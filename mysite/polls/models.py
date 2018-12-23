from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone


class Question ( models.Model ):
    question_text = models.CharField ( max_length=200 )
    pub_date = models.DateTimeField ( 'date published' )

    def __str__ ( self ):
        return self.question_text

    def was_published_recently ( self ):
        now = timezone.now ()
        return now - datetime.timedelta ( days=1 ) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.BooleanField = True
    was_published_recently.short_description = 'Published recently?'
    was_published_recently.empty_value_display = 'unknown'


class Choice ( models.Model ):
    question = models.ForeignKey(Question, on_delete=models.CASCADE )
    choice_text = models.CharField(max_length=200 )
    votes = models.IntegerField ( default=0 )
    gender = models.CharField(max_length=100, choices=(('F' , 'FEMALE'), ('M', 'MALE')) )

    def __str__ ( self ):
        return self.choice_text


class User (models.Model):

    name = models.CharField ( max_length=20 )
    username = models.EmailField ()
    password = models.CharField (max_length=5)

    def __str__ ( self ):
        return self.name
