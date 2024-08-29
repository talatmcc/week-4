from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_tasks, name='show_tasks'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
