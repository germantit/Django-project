from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('news/<slug:slug>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('contacts/', views.contacts.as_view(), name='contacts'),
    path('reviews/', views.ReviewsDetailView.as_view(), name='reviews'),
]
