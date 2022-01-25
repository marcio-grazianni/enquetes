from django.contrib import admin

from .models import Question
from .models import Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'pub_date', 'pub_time']
    list_editable = ['question_text', 'pub_date', 'pub_time']
    # list_filter = ('question_text', 'pub_date', 'pub_time')
    search_fields = ['question_text']

@admin.register(Choice)
class ChoicenAdmin(admin.ModelAdmin):
    list_display = ['id', 'choice_text', 'votes', 'question']
    list_editable = ['choice_text', 'votes', 'question']
    search_fields = ['choice_text']

# admin.site.register(Question)
# admin.site.register(Choice)
