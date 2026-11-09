from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Task
from .forms import TaskForm


# Dashboard
@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(is_completed=True).count()
    pending_tasks = tasks.filter(is_completed=False).count()

    productivity = (
        round((completed_tasks / total_tasks) * 100)
        if total_tasks else 0
    )

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'focus_hours': 0,
        'productivity': productivity,
    }

    return render(request, 'productivity/dashboard.html', context)


# View Tasks
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'productivity/tasks.html', {'tasks': tasks})


# Add Task
@login_required
def task_create(request):
    form = TaskForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        messages.success(request, 'Task added successfully!')
        return redirect('task_list')

    return render(request, 'productivity/task_form.html', {'form': form})


# Edit Task
@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    form = TaskForm(request.POST or None, instance=task)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('task_list')

    return render(request, 'productivity/task_form.html', {'form': form})


# Delete Task
@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')

    return render(
        request,
        'productivity/task_confirm_delete.html',
        {'task': task}
    )


# Complete / Pending Task
@login_required
def task_toggle(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.is_completed = not task.is_completed
        task.save()
    
    return redirect('task_list')


# Registration
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if not username or not email or not password:
            messages.error(request, 'Please fill in all fields.')

        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')

        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            login(request, user)
            return redirect('dashboard')

    return render(request, 'productivity/register.html')


# Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        messages.error(request, 'Invalid username or password.')

    return render(request, 'productivity/login.html')


# Logout
@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return redirect('dashboard')
