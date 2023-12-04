from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    first_name =None
    last_name = None
    LECTEUR = 'LECTEUR'
    AUTEUR = 'AUTEUR'

    ROLE_CHOICES = (
        (LECTEUR, 'Lecteur'),
        (AUTEUR, 'auteur')
    )
    

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='role')
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)
    biographie = models.CharField(max_length=250, null=True)
    photos = models.ImageField(upload_to='media/accounts',null=True)
    date_naissance = models.DateField(null=True)
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.nom} {self.prenom}'