from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_ap, name='catalog_ap'),
    path('catalog-ap/<slug:slug>/', views.FlatDetailView.as_view(), name='flat-detail'),
]
