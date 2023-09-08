from rest_framework import serializers
from .models import Task,Project,Owner,Tags

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields="__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields="__all__"

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Owner
        fields="__all__"