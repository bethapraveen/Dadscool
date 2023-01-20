from django.db import models

from django.utils.html import mark_safe

# Create your models here.

class PhysicsQuestion(models.Model):
	question_text = models.ImageField(upload_to='PhysicsQuestions')
	question_viewed_count=models.IntegerField(default='0')	
	question_id=models.AutoField(primary_key=True)
	pub_date = models.DateTimeField('date published')
	question_answer = models.ImageField(upload_to='PhysicsQuestions')
	def img_preview(self): #new
		return mark_safe(f'<img src = "{self.question_text.url}" />')
	def answer_preview(self): #new
		return mark_safe(f'<img src = "{self.question_answer.url}" />')



   