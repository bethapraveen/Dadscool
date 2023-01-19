from django.db import models

from django.utils.html import mark_safe

# Create your models here.

class Question(models.Model):
	question_text = models.ImageField(upload_to='Questions')
	pub_date = models.DateTimeField('date published')
	def img_preview(self): #new
		return mark_safe(f'<img src = "{self.question_text.url}" width = "300"/>')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.ImageField(upload_to='Answers')
    votes = models.IntegerField(default=0)


   