from django.db import models
from accounts.models import User
# Create your models here.

class Article_category(models.Model):
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    couverture = models.ImageField(upload_to='media', null=True) 

    def __str__(self) -> str:
        return self.nom
    
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    publier = models.BooleanField(default=False)
    image_couverture = models.ImageField(upload_to='media')
    date_publication = models.DateField(auto_now_add=True)
    auteur = models.ManyToManyField(User, related_name='articles')
    categorie = models.ManyToManyField(Article_category)

    def __str__(self) -> str:
        return self.titre