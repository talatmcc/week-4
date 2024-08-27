from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('student_form/', views.studentFrom, name='student-form'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('django_form/', views.django_form, name='Django-form'),
    path('model_form/', views.model_form, name='model-form'),
    path('delete/<int:roll>', views.delete_student, name='delete-student'),
]