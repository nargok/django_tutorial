from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = (
      (None, {
          "fields": (
              ['question_text']
          ),
      }),
      # classes : ['collapse']はHideリンクで要素を隠せるようにする
      ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
  )
  inlines = [ChoiceInline] # Choiceを同じ画面上で編集できるようにする
  list_display = ('question_text', 'pub_date', 'was_published_recently')
  list_filter = ['pub_date'] # サイドバーのフィルター機能
  search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)