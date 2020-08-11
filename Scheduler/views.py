from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework import status,generics
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
import json
# Create your views here.
@api_view(['GET'])
def get_Tasks(request):
    tasks=Task.objects.all()
    serializer=TaskSerializer(tasks,many=True)
    return JsonResponse({'Tasks':serializer.data},safe=False,status=status.HTTP_200_OK)


@api_view(['POST'])
def create_Tasks(request):
    payload=json.loads(request.body)
    try:
        task=Task.objects.create(
            task_type=payload["task_type"],
            task_desc=payload["task_desc"]
        )
        serializer=TaskSerializer(task)
        return JsonResponse({'Task':serializer.data},safe=False,status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({'error':str(e)},safe=False,status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_Tasks(request,task_id):
    payload=json.loads(request.body)
    try:
        if(int(payload["task_type"])>4): 
            return JsonResponse({'error':'Wrong Task Type'})
        else:
            task_item=Task.objects.filter(id=task_id)
            task_item.update(**payload)
            task=Task.objects.get(id=task_id)
            serializer=TaskSerializer(task)
            return JsonResponse({'book':serializer.data},safe=False,status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'error':str(e)},safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class getTasks(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer