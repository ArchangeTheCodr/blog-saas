from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('role choice/', views.role_choice, name='role_choice'),
    path('register/<str:rl>/', views.register_user, name='register'),
    path('update/<str:rl>/<int:id>/', views.update_user, name='update_user'),
    path('update/<int:user>/password/', views.update_password, name='update_password'),
    path('myaccount/<str:username>/', views.user_account, name='user_account')
]