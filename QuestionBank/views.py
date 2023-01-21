from django.http import HttpResponse
from django.views.generic import ListView
from .models import PhysicsQuestion
from .models import ChemistryQuestion
from .models import BiologyQuestion
from .models import MathsQuestion
from .models import StatisticsQuestion
import random

from django.shortcuts import render
from django.core.paginator import Paginator


def index(request):
	
	latest_question_list = list(PhysicsQuestion.objects.order_by('question_viewed_count','-pub_date')[:10])
	paginator=Paginator(latest_question_list,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	if request.GET.get('question') != None:
		question = PhysicsQuestion.objects.get(question_id=request.GET.get('question'))
		#question.update(question_viewed_count, question_viewed_count+1)
		question.question_viewed_count= question.question_viewed_count+1
		question.save(update_fields=['question_viewed_count'])

	return render(request, 'list.html', {'page_obj': page_obj})

def chemistry(request):
	
	latest_question_list = list(ChemistryQuestion.objects.order_by('question_viewed_count','-pub_date')[:10])
	paginator=Paginator(latest_question_list,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	if request.GET.get('question') != None:
		question = ChemistryQuestion.objects.get(question_id=request.GET.get('question'))
		#question.update(question_viewed_count, question_viewed_count+1)
		question.question_viewed_count= question.question_viewed_count+1
		question.save(update_fields=['question_viewed_count'])

	return render(request, 'list.html', {'page_obj': page_obj})


def biology(request):
	
	latest_question_list = list(BiologyQuestion.objects.order_by('question_viewed_count','-pub_date')[:10])
	paginator=Paginator(latest_question_list,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	if request.GET.get('question') != None:
		question = BiologyQuestion.objects.get(question_id=request.GET.get('question'))
		#question.update(question_viewed_count, question_viewed_count+1)
		question.question_viewed_count= question.question_viewed_count+1
		question.save(update_fields=['question_viewed_count'])

	return render(request, 'list.html', {'page_obj': page_obj})

def maths(request):
	
	latest_question_list = list(MathsQuestion.objects.order_by('question_viewed_count','-pub_date')[:10])
	paginator=Paginator(latest_question_list,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	if request.GET.get('question') != None:
		question = MathsQuestion.objects.get(question_id=request.GET.get('question'))
		#question.update(question_viewed_count, question_viewed_count+1)
		question.question_viewed_count= question.question_viewed_count+1
		question.save(update_fields=['question_viewed_count'])

	return render(request, 'list.html', {'page_obj': page_obj})

def statistics(request):
	
	latest_question_list = list(StatisticsQuestion.objects.order_by('question_viewed_count','-pub_date')[:10])
	paginator=Paginator(latest_question_list,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	if request.GET.get('question') != None:
		question = StatisticsQuestion.objects.get(question_id=request.GET.get('question'))
		#question.update(question_viewed_count, question_viewed_count+1)
		question.question_viewed_count= question.question_viewed_count+1
		question.save(update_fields=['question_viewed_count'])

	return render(request, 'list.html', {'page_obj': page_obj})

def RandomQuestion(request):
	QuestionBank=random.randint(1,5)
	if QuestionBank==1:
		number_of_records = PhysicsQuestion.objects.count()
		random_index = random.randint(4,4+number_of_records-1)
		latest_question_list = PhysicsQuestion.objects.get(pk = random_index)
	elif QuestionBank==2:
		number_of_records = ChemistryQuestion.objects.count()
		random_index = random.randint(1,number_of_records)
		latest_question_list = ChemistryQuestion.objects.get(pk = random_index)
	elif QuestionBank==3:
		number_of_records = BiologyQuestion.objects.count()
		random_index = random.randint(2,2+number_of_records-1)
		latest_question_list = BiologyQuestion.objects.get(pk = random_index)
	elif QuestionBank==4:
		number_of_records = MathsQuestion.objects.count()
		random_index = random.randint(7,7 + number_of_records -1)
		latest_question_list = MathsQuestion.objects.get(pk = random_index)
	elif QuestionBank==5:
		number_of_records = StatisticsQuestion.objects.count()
		random_index = random.randint(4,4+number_of_records-1)
		latest_question_list = StatisticsQuestion.objects.get(pk = random_index)

	paginator=Paginator(latest_question_list,1)
	#page_number = request.GET.get('page')
	page_obj = latest_question_list  #paginator.get_page(page_number)

	
	return render(request, 'randomQuestion.html', {'page_obj': page_obj})


