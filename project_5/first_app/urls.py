from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('first_app/about/', views.about, name='aboutpage'),
    path('form/', views.form, name='formpage'),
]
