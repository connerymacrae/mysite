from django.contrib import admin

# Register your models here.

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    fields = ["choice_text", "question", "votes"]


admin.site.register(Choice, ChoiceAdmin)
