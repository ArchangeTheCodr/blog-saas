from django.shortcuts import render
from blog.models import Article

def homepage(request):
    articles = Article.objects.all().order_by('-date_publication').filter(publier=True)[:6]
    return render(request, 'home.html', {'articles' : articles})