from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    
    path('PhysicsQuestions',views.index, name='index'),
    path('ChemistryQuestions',views.chemistry, name='chemistry'),
    path('BiologyQuestions',views.biology, name='biology'),
    path('MathsQuestions',views.maths, name='maths'),
    path('StatisticsQuestions',views.statistics, name='statistics'),
    path('',TemplateView.as_view(template_name='QuestionBank.html')), 
    path('RandomQuestion',views.RandomQuestion, name='random'),	
]

