from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('tasks', views.task_list, name='task_list'),  # Lista de tarefas
    path('create/', views.task_create, name='task_create'),  # Criar tarefa
    path('update/<int:pk>/', views.task_update, name='task_update'),  # Editar tarefa
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),  # Excluir tarefa
    path('completed/', views.completed_tasks, name='completed_tasks'),  # Tarefas Concluídas
]