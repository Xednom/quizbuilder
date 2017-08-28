from django.contrib import admin

from .models import Quiz, Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Quiz',               {'fields': ['quiz']}),
        ('Question',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['date_created']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
