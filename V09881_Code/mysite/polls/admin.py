from django.contrib import admin

from .models import Question
from .models import Choice


class ChoiceInstanceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'question_text', 'pub_date', ]
    inlines = [ChoiceInstanceInline]


admin.site.register(Question, QuestionAdmin)
