from django.urls import path, include
from . import views
app_name = 'blog_app'

urlpatterns = [
    path('articles/', views.article, name='article'),
    path('articles/<int:id>/', views.detail_article, name='detail_article'),
    path('articles/create/', views.create_article, name='create_article'),
    path('articles/update/<int:key>/', views.update_article, name='update_article'),
    path('articles/delete/<int:key>/', views.delete_article, name='delete_article'),
    path('auteurs/', views.auteur, name='auteur'),
    path('auteurs/<int:id>/', views.detail_auteur, name='detail_auteur'),
    path('categories/', views.categorie_article, name='categorie_article'),
]