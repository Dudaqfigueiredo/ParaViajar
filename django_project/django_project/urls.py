"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from users.views import register
from .views import index
from .views import business
from blog.views import contants
from blog.views import about
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostYearArchiveView
from django.contrib.auth import views as auth_views
from django.views.generic.dates import ArchiveIndexView
from blog.models import Post


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('', index),
    path('blog/', include('blog.urls')),
    path('register/', register),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('business', PostListView.as_view(), name='business'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(),name='post-delete'),
    path('archive/', ArchiveIndexView.as_view(model=Post, date_field="data"), name="post_archive"),
    path('<int:year>/', PostYearArchiveView.as_view(), name="post_year_archive"),
    path('about/', about, name='about'),
    path('contants/', contants, name='contants')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)