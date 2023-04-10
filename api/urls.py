from django.urls import path
from . import views

urlpatterns = [
    path("todos/", views.TodoList.as_view(), name="list"),
    path("todos/create", views.TodoListCreate.as_view(), name="create"),
    path("todos/<int:pk>", views.TodoRetrieveUpdateDestroy.as_view(), name="edit"),
    path("todos/<int:pk>/complete", views.TodoToggleComplete.as_view(), name="complete"),
    path("signup/", views.signup),
    path("login/", views.login),
]
