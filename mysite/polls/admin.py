
# Register your models here.
from django.contrib import admin
from .models import Question , Choice,User


class ChoiceInline ( admin.TabularInline ):
    model = Choice
    extra = 3


class QuestionAdmin ( admin.ModelAdmin ):
    fieldsets = [
        (None , {'fields': [ 'question_text' ]}) ,
        ('Date information' , {'fields': [ 'pub_date' ] , 'classes': [ 'collapse' ]}) ,
    ]
    list_display = ('question_text' , 'pub_date' , 'was_published_recently')
    inlines = [ ChoiceInline ]
    empty_value_display = 'unknown'
    list_filter = [ 'pub_date' ]
    search_fields = [ 'question_text' ]
    actions = 'was_published_recently'
    ordering = [ 'pub_date' ]


class ChoiceAdmin ( admin.ModelAdmin ):
    fields = [ 'question' , 'choice_text' , 'votes' , 'gender' ]
    radio_fields = {'gender': admin.VERTICAL}
    autocomplete_fields = ['question']


admin.site.register ( Question , QuestionAdmin )

admin.site.register ( Choice , ChoiceAdmin )

admin.site.register(User)