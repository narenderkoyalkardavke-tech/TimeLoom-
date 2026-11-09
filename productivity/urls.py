from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.task_create, name='task_create'),
    path('tasks/edit/<int:task_id>/', views.task_update, name='task_update'),
    path('tasks/delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('tasks/toggle/<int:task_id>/', views.task_toggle, name='task_toggle'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]