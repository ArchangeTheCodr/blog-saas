from django import forms
from .models import *


class CreateArticleForm(forms.ModelForm):
    rlAuteur = User.objects.all().filter(role='AUTEUR') 
    auteur = forms.ModelMultipleChoiceField(queryset=rlAuteur)
    class Meta:
        model = Article
        fields = [
            'titre',
            'contenu',
            'categorie',
            'image_couverture',
            'publier'
        ]


