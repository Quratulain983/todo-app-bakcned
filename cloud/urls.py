from django.urls import path
from .views import get_todos, add_todo, delete_todo

urlpatterns = [
    path('todos/', get_todos),
    path('todos/add/', add_todo),
    path('todos/delete/<int:pk>/', delete_todo),
]