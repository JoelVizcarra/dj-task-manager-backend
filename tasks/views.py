from rest_framework import viewsets
from django.contrib.auth.models import User

from tasks.models import Tag, State, Task, Project
from tasks.serializers import (
    UserSerializer,
    ProjectSerializer,
    TagSerializer,
    StateSerializer,
    TaskSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    View for User model
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    View for Project model
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class TagViewSet(viewsets.ModelViewSet):
    """
    View for Tag model
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class StateViewSet(viewsets.ModelViewSet):
    """
    View for State model
    """
    queryset = State.objects.all()
    serializer_class = StateSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    View for Task model
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
