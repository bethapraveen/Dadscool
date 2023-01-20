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

class ChemistryQuestion(models.Model):
	question_text = models.ImageField(upload_to='ChemistryQuestions')
	question_viewed_count=models.IntegerField(default='0')	
	question_id=models.AutoField(primary_key=True)
	pub_date = models.DateTimeField('date published')
	question_answer = models.ImageField(upload_to='ChemistryQuestions')
	def img_preview(self): #new
		return mark_safe(f'<img src = "{self.question_text.url}" />')
	def answer_preview(self): #new
		return mark_safe(f'<img src = "{self.question_answer.url}" />')

class BiologyQuestion(models.Model):
	question_text = models.ImageField(upload_to='BiologyQuestion')
	question_viewed_count=models.IntegerField(default='0')	
	question_id=models.AutoField(primary_key=True)
	pub_date = models.DateTimeField('date published')
	question_answer = models.ImageField(upload_to='BiologyQuestion')
	def img_preview(self): #new
		return mark_safe(f'<img src = "{self.question_text.url}" />')
	def answer_preview(self): #new
		return mark_safe(f'<img src = "{self.question_answer.url}" />')

class MathsQuestion(models.Model):
	question_text = models.ImageField(upload_to='MathsQuestion')
	question_viewed_count=models.IntegerField(default='0')	
	question_id=models.AutoField(primary_key=True)
	pub_date = models.DateTimeField('date published')
	question_answer = models.ImageField(upload_to='MathsQuestion')
	def img_preview(self): #new
		return mark_safe(f'<img src = "{self.question_text.url}" />')
	def answer_preview(self): #new
		return mark_safe(f'<img src = "{self.question_answer.url}" />')

class StatisticsQuestion(models.Model):
	question_text = models.ImageField(upload_to='StatisticsQuestion')
	question_viewed_count=models.IntegerField(default='0')	
	question_id=models.AutoField(primary_key=True)
	pub_date = models.DateTimeField('date published')
	question_answer = models.ImageField(upload_to='StatisticsQuestion')
	def img_preview(self): #new
		return mark_safe(f'<img src = "{self.question_text.url}" />')
	def answer_preview(self): #new
		return mark_safe(f'<img src = "{self.question_answer.url}" />')

