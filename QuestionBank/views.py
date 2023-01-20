from django.http import HttpResponse
from django.views.generic import ListView
from .models import PhysicsQuestion
from django.shortcuts import render
from django.core.paginator import Paginator


def index(request):
	latest_question_list = PhysicsQuestion.objects.order_by('-pub_date')[:5]
	paginator=Paginator(latest_question_list,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'list.html', {'page_obj': page_obj})