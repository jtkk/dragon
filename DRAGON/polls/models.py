import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):              # __unicode__ on Python 2
        return u'%s' %  (self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):              # __unicode__ on Python 2
        return u'%s' % (self.choice_text)



# class Question(models.Model):
#      # ...
#      def was_published_recently(self):
#          return self.pub_date >= timezone.now() - datetime.timedelta(days=1)