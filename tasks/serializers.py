from rest_framework import serializers
from django.contrib.auth.models import User

from tasks.models import Tag, State, Task, Project


class AuthStampedSerializer(serializers.ModelSerializer):
    read_only_fields = ('id', 'created_by', 'created_at', 'updated_by', 'updated_at',)

    class Meta:
        abstract = True
    
    def create(self, validated_data):
        user = self.context['request'].user
        if not user.is_anonymous:
            validated_data['created_by'] = user
            validated_data['updated_by'] = user

        return super(AuthStampedSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if not user.is_anonymous:
            validated_data['updated_by'] = user

        return super(AuthStampedSerializer, self).update(instance, validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class TaskSerializer(AuthStampedSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(AuthStampedSerializer):
    class Meta:
        model = Project
        fields = '__all__'