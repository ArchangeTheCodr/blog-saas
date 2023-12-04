from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.http import urlencode
from django.shortcuts import render, redirect
from django.urls import reverse
from .filters import ArticleFilter, AuteurFilter, ArticleFilterComplete
from .forms import CreateArticleForm
from accounts.models import User
from .models import Article, Article_category


def article(request):
    articles = Article.objects.all()  
    myFilter = ArticleFilterComplete(request.GET, queryset = articles)
    articles = myFilter.qs
    base_url = reverse('blog_app:article')
    url_parameter = {
        'titre' : request.GET.get('titre', ''),
        'categorie' : request.GET.get('article', ''),
        'auteur' : request.GET.get('auteur', ''),
        'date_publication' : request.GET.get('date_publication', ''),  
        }
    query_string = urlencode(url_parameter)
    url = f'{base_url}?{query_string}'
    redirect(url)

    paginator = Paginator(articles, 2)
    num_page = request.GET.get('page')
    page_actuel = paginator.get_page(num_page)
    context = {'myFilter' : myFilter, 'page_actuel' : page_actuel}
    return render(request, 'blog/home.html', context)

@login_required
def detail_article(request, id):
    article = Article.objects.get(pk=id)
    recommandations = Article.objects.filter(
        categorie=article.categorie.get(), 
        auteur=article.auteur.get()
    )
    recommandations = recommandations.exclude(pk=id)[:12]
    return render(request, 'blog/detail_article.html', {'article' : article, 'recommandations' : recommandations})

@permission_required('blog_app.add_article')
def create_article(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            titre = request.POST.get('titre')
            contenu = request.POST.get('contenu')
            auteur = request.POST.get('auteur')
            categorie = request.POST.get('categorie')
            publier = request.POST.get('publier')
            image_couverture = request.FILES.get('image_couverture')

            if publier == 'on':
                publier = True
            else:
                publier = False

            art = Article.objects.create(
                titre=titre,
                contenu=contenu,
                publier=publier,
                image_couverture=image_couverture,
            )
            art.auteur.set(auteur)
            art.categorie.set(categorie)
            art.save()
            return redirect('homepage')
    else:
        form = CreateArticleForm()

    return render(request, 'blog/create_article.html', {'form' : form})

@permission_required('blog_app.change_article')
def update_article(request, key):
    article = Article.objects.get(pk=key)
    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = CreateArticleForm(instance=article)
        
    return render(request, 'blog/create_article.html', {'form' : form})

@permission_required('blog_app.delete_article')
def delete_article(request, key):
    article = Article.objects.get(pk = key)
    article.delete()
    return redirect('homepage')

def auteur(request):
    auteurs = User.objects.all().filter(role = 'AUTEUR')
    myFilter = AuteurFilter(request.GET, queryset = auteurs)
    auteurs = myFilter.qs
    base_url = reverse('blog_app:auteur')
    url_parameter = {
        'nom' : request.GET.get('nom', ''),
        'prenom' : request.GET.get('prenom', ''),
        'date_inscription' : request.GET.get('date_inscription', '')
    }
    query_string = urlencode(url_parameter)
    url = f'{base_url}?{query_string}'
    redirect(url)

    paginator = Paginator(auteurs, 1)
    num_page = request.GET.get('page')
    page_actuel = paginator.get_page(num_page)
    context = {'page_actuel' : page_actuel,  'myFilter' : myFilter}
    return render(request, 'blog/auteur.html', context)



@login_required
def detail_auteur(request, id):
    auteur = User.objects.all().filter(role = 'AUTEUR').get(pk=id)
    articles = Article.objects.all().filter(auteur = id)
    myFilter = ArticleFilter(request.GET, queryset = articles)
    articles = myFilter.qs
    base_url = reverse('blog_app:detail_auteur', args=(id,))
    url_parameter = {
        'titre' : request.GET.get('titre', ''),
        'categorie' : request.GET.get('categorie', '')
    }
    query_string = urlencode(url_parameter)
    url = f'{base_url}?{query_string}'
    redirect(url)

    paginator = Paginator(articles, 2)
    num_page = request.GET.get('page')
    page_actuel = paginator.get_page(num_page)
    context = {'page_actuel' : page_actuel, 'auteur' : auteur, 'myFilter' : myFilter}
    return render(request, 'blog/detail_auteur.html', context)