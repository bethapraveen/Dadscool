from django.contrib import admin

# Register your models here.

from .models import PhysicsQuestion
from .models import ChemistryQuestion
from .models import BiologyQuestion
from .models import MathsQuestion
from .models import StatisticsQuestion



fields = ['image_tag']
readonly_fields = ['image_tag']

class PhysicsQuestionAdmin(admin.ModelAdmin): # new
     readonly_fields = ['img_preview','answer_preview']


class ChemistryQuestionAdmin(admin.ModelAdmin): # new
     readonly_fields = ['img_preview','answer_preview']


class BiologyQuestionAdmin(admin.ModelAdmin): # new
     readonly_fields = ['img_preview','answer_preview']


class MathsQuestionAdmin(admin.ModelAdmin): # new
     readonly_fields = ['img_preview','answer_preview']


class StatisticsQuestionAdmin(admin.ModelAdmin): # new
     readonly_fields = ['img_preview','answer_preview']

admin.site.register(PhysicsQuestion,PhysicsQuestionAdmin)
admin.site.register(ChemistryQuestion,ChemistryQuestionAdmin)
admin.site.register(BiologyQuestion,BiologyQuestionAdmin)
admin.site.register(MathsQuestion,MathsQuestionAdmin)
admin.site.register(StatisticsQuestion,StatisticsQuestionAdmin)