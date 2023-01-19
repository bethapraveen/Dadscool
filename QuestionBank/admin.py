from django.contrib import admin

# Register your models here.

from .models import Question



fields = ['image_tag']
readonly_fields = ['image_tag']

class QuestionAdmin(admin.ModelAdmin): # new
     readonly_fields = ['img_preview']

admin.site.register(Question,QuestionAdmin)