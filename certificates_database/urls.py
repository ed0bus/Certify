from django.urls import path
from . import views
from .views import search_results_view

urlpatterns = [path('', views.index, name='certificates_index'),
               path('search/', views.search_results_view, name='search_results')] #ricerca txId
