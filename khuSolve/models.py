from django.db import models

# Create your models here.
class Problems(models.Model):
  title = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  body = models.TextField()
  answer = models.TextField()

  def __str__(self):
    return self.title

class UserAnswer(models.Model):
  useranswer = models.TextField()

  def __str__(self):
    return self.useranswer
