from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def show_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'task/show_tasks.html', {'data': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('show_tasks')
