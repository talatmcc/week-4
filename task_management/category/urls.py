from django.urls import path
from . import views

urlpatterns = [
    path('categories/add/', views.add_category, name='add_category'),
]
