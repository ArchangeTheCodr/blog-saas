from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from blog_saas import settings

app_name = 'blog_saas'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('blog/', include('blog.urls',namespace='blog_app')),
    path('accounts/', include('accounts.urls',namespace='accounts')),
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
