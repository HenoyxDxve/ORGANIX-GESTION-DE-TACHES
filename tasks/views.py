from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            form.save()  # connexion automatique après inscription
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def task_list(request):

    # Récupérer toutes les tâches de l'utilisateur
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')

    # Statistiques
    tasks_in_progress_count = Task.objects.filter(status='in_progress', user=request.user).count()
    tasks_done_count = Task.objects.filter(status='done', user=request.user).count()
    tasks_high_priority_count = Task.objects.filter(priority='high', user=request.user).count()

    context = {
        'tasks': tasks,
        'tasks_in_progress_count': tasks_in_progress_count,
        'tasks_done_count': tasks_done_count,
        'tasks_high_priority_count': tasks_high_priority_count,
    }

    return render(request, 'tasks/task_list.html', context)

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Créer'})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Modifier'})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


def task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.status = 'done' if task.status != 'done' else 'todo'
    task.save()
    return redirect('task_list')


