from django.urls import path
from . import views
from django.contrib import admin
from .views import index
from .views import business
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
from users import views as user_views

from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.index, name='index'),
    path('business', PostListView.as_view(), name='business'),
    path('register', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='post-update'),
]


