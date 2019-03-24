from django import forms
from .models import Articles
from django.http import HttpResponseRedirect
from taggit.forms import TagField
from django.http import JsonResponse

class PostForm(forms.ModelForm):
    #описывает модель для которой делается форма
    class Meta:  
        model = Articles
        fields = ('author','title', 'post', 'category', 'image', 'tags')

class EditPostForm(forms.ModelForm):
    #описывает модель для которой делается форма
    class Meta:  
        model = Articles
        fields = ('author','title', 'post', 'category', 'image', 'tags')
