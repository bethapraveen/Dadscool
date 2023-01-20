from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    
    path('PhysicsQuestions',views.index, name='index'),
    path('ChemistryQuestions',views.index, name='chemistry'),
    path('BiologyQuestions',views.index, name='biology'),
    path('MathsQuestions',views.index, name='maths'),
    path('StatisticsQuestions',views.index, name='statistics'),
    path('',TemplateView.as_view(template_name='QuestionBank.html')), 
]

