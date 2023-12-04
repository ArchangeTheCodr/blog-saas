import django_filters as filters
from django import forms

from .models import *

class ArticleFilter(filters.FilterSet):
    titre = filters.CharFilter(
        field_name='titre', 
        lookup_expr='icontains', 
        label='Titre', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    categorie = filters.ModelChoiceFilter(
        queryset=Article_category.objects.all(), 
        label='Categorie', 
        widget = forms.Select(attrs={'class': 'form-select'}),    
    )
    class Meta:
        model = Article
        exclude = ['image_couverture','contenu', 'publier','date_publication', 'auteur']
    
class AuteurFilter(filters.FilterSet):
    nom = filters.CharFilter(
        field_name = 'nom',
        lookup_expr = 'icontains',
        label = 'Nom',
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'entrer un nom',
                'class' : 'form-control',
            }
        )
    )
    prenom = filters.CharFilter(
        field_name = 'prenom',
        lookup_expr = 'icontains',
        label = 'Prenom',
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'entrer un prenom',
                'class' : 'form-control',
            }
        )
    )
    date_inscription_min= filters.DateFilter(
        field_name = 'date_inscription',
        label = 'date d\'inscription minimal',
        lookup_expr = 'gte',
        widget = forms.DateInput(attrs={'class' : 'form-control'})
    )
    date_inscription_max = filters.DateFilter(
        field_name = 'date_inscription',
        label = 'date d\'inscription maximal',
        lookup_expr = 'lte',
        widget = forms.DateInput(attrs={'class' : 'form-control'})
    )
    class Meta:
        model = User
        # fields = ['nom','prenom']
        exclude = [
            'biographie', 'email', 'photos', 'date_naissance',
            'date_inscription', 'is_active', 'last_login', 'password',
            'username', 'role',  'statut','is_superuser', 'groups',
            'user_permissions', 'is_staff', 'date_joined',   
        ]


class ArticleFilterComplete(filters.FilterSet):
    titre = filters.CharFilter(
        field_name='titre', 
        lookup_expr='icontains', 
        label='Titre', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    article = filters.ModelChoiceFilter(
        queryset = Article_category.objects.all(), 
        label='Categorie', 
        widget = forms.Select(attrs={'class': 'form-select'}),    
    )
    auteur = filters.ModelChoiceFilter(
        queryset = User.objects.all().filter(role = 'AUTEUR'),
        label = 'Auteur',
        widget = forms.Select(attrs={'class' : 'form-select'})
    )
    date_publication_min = filters.DateFilter(
        field_name = 'date_publication',
        label = 'date minimal de publication ',
        lookup_expr = 'gte',
        widget = forms.DateInput(attrs={'class' : 'form-control'})
    )
    date_publication_max = filters.DateFilter(
        field_name = 'date_publication',
        label = 'date maximal de publication',
        lookup_expr = 'lte',
        widget = forms.DateInput(attrs={'class' : 'form-control'})
    )
    class Meta:
        model = Article
        exclude = ['image_couverture','contenu', 'publier', 'date_publication', 'categorie',]