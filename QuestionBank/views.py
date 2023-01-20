from django.http import HttpResponse
from django.views.generic import ListView
from .models import PhysicsQuestion
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

