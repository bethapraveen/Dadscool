from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    
    path('PhysicsQuestions',views.index, name='index'),
    path('ChemistryQuestions',views.index, name='index'),
    path('BiologyQuestions',views.index, name='index'),
    path('MathsQuestions',views.index, name='index'),
    path('StatisticsQuestions',views.index, name='index'),
    path('',TemplateView.as_view(template_name='QuestionBank.html')), 
]

