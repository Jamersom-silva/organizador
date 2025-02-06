from django.contrib import admin
from django.urls import path, include  # 'include' é importante para incluir as URLs do app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # Incluir as URLs do app 'tasks'
]
