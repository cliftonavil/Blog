from django import forms
from .import models


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Articles
        fields = ['tittle', 'body', 'slug', 'thumb']
