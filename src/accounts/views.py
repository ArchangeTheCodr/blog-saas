from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LecteurCreationForm, AuteurCreationForm, UserUpdateForm
from django.shortcuts import render, redirect
from .models import *
from blog.models import Article
from django.utils.http import urlencode
from django.urls import reverse
from django.core.paginator import Paginator
from blog.filters import ArticleFilter


# Create your views here.


def login_user(request):
    if request.method == 'POST':
        Uname = request.POST['username']
        Pword = request.POST['password'] 
        user = authenticate(request, username = Uname, password = Pword)

        if  user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Informations incorrect !')

    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : form})

def logout_user(request):
    logout(request)
    return redirect('homepage')

def role_choice(request):
    return render(request, 'accounts/role_choice.html')

def register_user(request, rl):
    if request.method == 'POST':
        if rl == 'AUTEUR':
            form = AuteurCreationForm(request.POST, request.FILES)
            group = Group.objects.get(name__iexact='auteur')
        else: 
            form = LecteurCreationForm(request.POST, request.FILES)
            group = Group.objects.get(name__iexact='lecteur')
        if form.is_valid():
            form.save()
            usr = request.POST.get('username')
            user = User.objects.get(username=usr)
            user.groups.add(group)
            
            return redirect('homepage')
    else:
        if rl == 'AUTEUR':
            form = AuteurCreationForm()
        else: 
            form = LecteurCreationForm()
        
    return render(request, 'accounts/register.html', {'form' : form})


def update_user(request, rl, id):
    auteur = User.objects.get(pk=id)
    lecteur = User.objects.get(pk=id)

    if request.method == 'POST':
        if rl == 'AUTEUR':
            form = UserUpdateForm(request.POST, request.FILES, instance = auteur)
        else: 
            form = UserUpdateForm(request.POST, request.FILES, instance = lecteur)

        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        if rl == 'AUTEUR':
            form = UserUpdateForm(instance = auteur)
        else: 
            form = UserUpdateForm(instance = lecteur)
        
    return render(request, 'accounts/user_update.html', {'form' : form})


def user_account(request, username):
    user = User.objects.get(username=username)
    articles = Article.objects.all().filter(auteur = user)
    myFilter = ArticleFilter(request.GET, queryset = articles)
    articles = myFilter.qs
    base_url = reverse('accounts:user_account', args=(id,))
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
    context = {'user' : user, 'page_actuel' : page_actuel,'myFilter' : myFilter}
    return render(request, 'accounts/user_acccount.html', context=context)

def update_password(request, user):
    usr = User.objects.get(pk=user)
    form = PasswordChangeForm(user=usr)
    return render(request, 'accounts/update_password.html', {'form' : form})