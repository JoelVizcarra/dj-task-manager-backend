from django.db import models
from django.contrib.auth.models import User


class AuthStampedModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True,
        blank=True, related_name='+')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True,
        blank=True, related_name='+')
    
    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Project(TimeStampedModel, AuthStampedModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    collaborators = models.ManyToManyField(User, blank=True,
        related_name='projects_collaboration',
        related_query_name='project_collaboration')
    administrators = models.ManyToManyField(User, blank=True,
        related_name='projects_administration',
        related_query_name='project_administration')


class Tag(TimeStampedModel):
    name = models.CharField(max_length=50)


class State(TimeStampedModel):
    name = models.CharField(max_length=50)


class Task(TimeStampedModel, AuthStampedModel):
    title = models.CharField(max_length=250)
    description = models.TextField()
    estimation = models.PositiveIntegerField()
    time_spend = models.PositiveIntegerField()
    due_date = models.DateField()
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
        blank=True, related_name='tasks', related_query_name='task')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='tasks', related_query_name='task')
    tags = models.ManyToManyField(Tag, blank=True, related_name='tasks',
        related_query_name='task')
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
        related_name='tasks', related_query_name='task')