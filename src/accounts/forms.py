from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User
from django import forms

class LecteurCreationForm(UserCreationForm):
    nom = forms.CharField(
        label = 'Nom',
        widget = forms.TextInput(attrs={'class' : 'form-control'})
    )
    prenom = forms.CharField(
        label = 'Prenom',
        widget = forms.TextInput(attrs={'class' : 'form-control'})
    )
    username = forms.CharField(
        label = 'Nom d\'utilisateur', 
        required=True, 
        widget = forms.TextInput(attrs={'class' : 'form-control'})
    )
    email = forms.EmailField(
        label='Adresse email', 
        required=True,
        widget = forms.EmailInput(attrs={'class' : 'form-control'})
    )
    photos = forms.ImageField(
        widget = forms.FileInput(attrs={'class' : 'form-control'})
    )
    ROLE_CHOICES = (
        ('LECTEUR', 'Lecteur'),
    )
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget = forms.Select(attrs={'class' : 'form-control'})    
    )
    password1 = forms.CharField(
        label='Mot de passe :',
        widget = forms.PasswordInput(attrs={'class' : 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirmation du mot de passe :',
        widget = forms.PasswordInput(attrs={'class' : 'form-control'})
    )

    class Meta:
        model = User
        fields = (
            'nom', 'prenom',
            'username','email', 
            'photos','role', 
            'password1', 'password2',
        ) 
       
        

class AuteurCreationForm(UserCreationForm):
    nom = forms.CharField(
        label = 'Nom', 
        required=True, 
        widget = forms.TextInput(attrs={'class' : 'form-control'})
    )
    prenom = forms.CharField(
        label = 'Prenom', 
        required=True, 
        widget = forms.TextInput(attrs={'class' : 'form-control'})
    )
    username = forms.CharField(
        label = 'Nom d\'utilisateur', 
        required=True, 
        widget = forms.TextInput(attrs={'class' : 'form-control'})
    )
    email = forms.EmailField(
        label='Adresse email', 
        required=True, 
        widget = forms.EmailInput(attrs={'class' : 'form-control'})
    )
    # photos = forms.FileField(
    #     widget = forms.FileInput(attrs={'class' : 'form-control'})
    # )
    ROLE_CHOICES = (
        ('AUTEUR', 'auteur'),
    )
    role = forms.ChoiceField(
        choices=ROLE_CHOICES, 
        widget = forms.Select(attrs={'class' : 'form-control'})
    )
    password1 = forms.CharField(
        label='Mot de passe :',
        widget = forms.PasswordInput(attrs={'class' : 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirmation du mot de passe :',
        widget = forms.PasswordInput(attrs={'class' : 'form-control'})
    )

    class Meta:
        model = User
        fields = (
            'nom', 'prenom',
            'username','email', 
            'photos','role', 
            'password1', 'password2',
        ) 
       

class UserUpdateForm(UserChangeForm):
    nom = forms.CharField(
        label = 'Nom', 
        required=True, 
        widget = forms.TextInput(attrs={'class' : 'form-control'})
    )
    prenom = forms.CharField(
        label = 'Prenom', 
        required=True, 
        widget = forms.TextInput(attrs={'class' : 'form-control'})
    )
    username = forms.CharField(
        label = 'Nom d\'utilisateur', 
        required=True, 
        widget = forms.TextInput(attrs={'class' : 'form-control'})
    )
    email = forms.EmailField(
        label='Adresse email', 
        required=True, 
        widget = forms.EmailInput(attrs={'class' : 'form-control'})
    )
    photos = forms.ImageField(
        widget = forms.FileInput(attrs={'class' : 'form-control'})
    )
    ROLE_CHOICES = (
        ('AUTEUR', 'auteur'),
    )
    role = forms.ChoiceField(
        choices=ROLE_CHOICES, 
        widget = forms.Select(attrs={'class' : 'form-control'})
    )
    class Meta:
        model = User
        fields = (
            'nom', 'prenom',
            'username','email', 
            'photos','role',
        ) 
        help_text = None