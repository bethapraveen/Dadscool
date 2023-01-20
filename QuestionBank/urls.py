from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    
    path('PhysicsQuestions',views.index, name='index'),
    path('',TemplateView.as_view(template_name='QuestionBank.html')), 
]

