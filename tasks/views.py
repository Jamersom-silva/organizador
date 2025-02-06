from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()  # Obtém todas as tarefas
    return render(request, 'tasks/task_list.html', {'tasks': tasks})  # Passa para o template

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redireciona para a lista de tarefas após salvar
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

def home(request):
    return render(request, 'home/home.html')


def completed_tasks(request):
    tasks = Task.objects.filter(completed=True)  # Filtra tarefas concluídas
    return render(request, 'tasks/completed_tasks.html', {'tasks': tasks})
    