from rest_framework import serializers
from .models import TaskTracker,Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"

class TaskTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskTracker
        fields="__all__"