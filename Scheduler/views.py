from django.shortcuts import render
from rest_framework import routers,viewsets
from .serializers import *
from .models import *



class TaskView(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

class TaskTrackerView(viewsets.ModelViewSet):
    queryset=TaskTracker.objects.all()
    serializer_class=TaskTrackerSerializer

router=routers.DefaultRouter()
router.register(r'task',TaskView)
router.register(r'tracker',TaskTrackerView)