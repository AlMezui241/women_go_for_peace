# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('categorie/<slug:category_slug>/', views.PostListByCategoryView.as_view(), name='list_by_category'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
]