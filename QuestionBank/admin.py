from django.contrib import admin

# Register your models here.

from .models import PhysicsQuestion



fields = ['image_tag']
readonly_fields = ['image_tag']

class PhysicsQuestionAdmin(admin.ModelAdmin): # new
     readonly_fields = ['img_preview','answer_preview']

admin.site.register(PhysicsQuestion,PhysicsQuestionAdmin)