from django.http import HttpResponse
from django.views.generic import ListView
from .models import PhysicsQuestion
from .models import ChemistryQuestion
from .models import BiologyQuestion
from .models import MathsQuestion
from .models import StatisticsQuestion
import random
from django.db.models import F

from django.shortcuts import render
from django.core.paginator import Paginator


def index(request):
	if request.GET.get('page') == None:
		PhysicsQuestion.objects.update(question_viewed_count=F('question_viewed_count_new'))
	latest_question_list = list(PhysicsQuestion.objects.order_by('question_viewed_count','-pub_date')[:10])
	paginator=Paginator(latest_question_list,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	page_obj[0].question_viewed_count_new= page_obj[0].question_viewed_count_new+1
	page_obj[0].save(update_fields=['question_viewed_count_new'])	
	return render(request, 'list.html', {'page_obj': page_obj})

def chemistry(request):

	if request.GET.get('page') == None:
		ChemistryQuestion.objects.update(question_viewed_count=F('question_viewed_count_new'))
	
	latest_question_list = list(ChemistryQuestion.objects.order_by('question_viewed_count','-pub_date')[:10])
	paginator=Paginator(latest_question_list,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	page_obj[0].question_viewed_count_new= page_obj[0].question_viewed_count_new+1
	page_obj[0].save(update_fields=['question_viewed_count_new'])	
	return render(request, 'list.html', {'page_obj': page_obj})

def biology(request):
	if request.GET.get('page') == None:
		BiologyQuestion.objects.update(question_viewed_count=F('question_viewed_count_new'))	
	latest_question_list = list(BiologyQuestion.objects.order_by('question_viewed_count','-pub_date')[:10])
	paginator=Paginator(latest_question_list,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	page_obj[0].question_viewed_count_new= page_obj[0].question_viewed_count_new+1
	page_obj[0].save(update_fields=['question_viewed_count_new'])	
	return render(request, 'list.html', {'page_obj': page_obj})

def maths(request):
	if request.GET.get('page') == None:
		MathsQuestion.objects.update(question_viewed_count=F('question_viewed_count_new'))
	latest_question_list = list(MathsQuestion.objects.order_by('question_viewed_count','-pub_date')[:10])
	paginator=Paginator(latest_question_list,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	page_obj[0].question_viewed_count_new= page_obj[0].question_viewed_count_new+1
	page_obj[0].save(update_fields=['question_viewed_count_new'])	
	return render(request, 'mathsList.html', {'page_obj': page_obj})

def statistics(request):
	if request.GET.get('page') == None:
		StatisticsQuestion.objects.update(question_viewed_count=F('question_viewed_count_new'))
	latest_question_list = list(StatisticsQuestion.objects.order_by('question_viewed_count','-pub_date')[:10])
	paginator=Paginator(latest_question_list,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	page_obj[0].question_viewed_count_new= page_obj[0].question_viewed_count_new+1
	page_obj[0].save(update_fields=['question_viewed_count_new'])	
	return render(request, 'mathsList.html', {'page_obj': page_obj})

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
	page_obj = latest_question_list 
	page_obj.question_viewed_count_new= page_obj.question_viewed_count_new+1
	page_obj.save(update_fields=['question_viewed_count_new'])
	
	return render(request, 'randomQuestion.html', {'page_obj': page_obj})


