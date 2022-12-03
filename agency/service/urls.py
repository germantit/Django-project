from django.urls import path
from . import views

urlpatterns = [
    path('', views.service, name='service'),
    path('catalog-nb/', views.catalog_nb, name='catalog_nb'),
    path('catalog-nb/<slug:slug>/', views.ComplexDetailView.as_view(), name='complex-detail'),
    path('sell/', views.Sell.as_view(), name='sell'),

]
