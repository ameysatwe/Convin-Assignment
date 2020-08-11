from django.shortcuts import render
from .serializers import *
from .models import Task
from rest_framework import status,generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
import json
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET'])
def get_Tasks(request):
    tasks=Task.objects.all()
    serializer=TaskSerializer(tasks,many=True)
    return JsonResponse({'Tasks':serializer.data})
@api_view(['GET'])
def get_One(request,id):
    tasks=Task.objects.get(id=id)
    serializers=TaskSerializer(tasks)
    return JsonResponse({'Tasks':serializers.data})
@api_view(['POST'])
def create_Tasks(request):
    payload=json.loads(request.body)
    print(payload)
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

@api_view(["POST"])
def createTaskTracker(request):
    serializer=TaskTrackerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)

    return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# class getTasks(generics.ListCreateAPIView):
#     queryset=Task.objects.all()
#     serializer_class=TaskSerializer
class getTaskTrackers(generics.ListCreateAPIView):
    queryset=TaskTracker.objects.all()
    serializer_class=TaskTrackerSerializer
class updateTrackers(generics.UpdateAPIView):
    pass


# class TaskList(APIView):
#     renderer_classes=[TemplateHTMLRenderer]
#     template_name='task_list.html'

#     def get(self,request):
#         task=Task.objects.all()
#         # serializer=TaskSerializer(task)
#         return render(request,'task_list.html',{'tasks':task})
#         #return HttpResponse({'tasks':task})


# class TaskDetail(APIView):
#     renderer_classes=[TemplateHTMLRenderer]
#     template_name='task_detail.html'

#     def get(self,request):
#         task=Task.objects.all()
#         # serializer=TaskSerializer(task)
#         return render(request,'task_detail.html',{'tasks':task})
#         #return HttpResponse({'tasks':task})

#     def post(self, request, pk):
#         task = get_object_or_404(Task)
#         serializer = TaskSerializer(task, data=request.data)
#         if not serializer.is_valid():
#             return HttpResponse({'serializer': serializer.data})
#         serializer.save()
#         return HttpResponseRedirect('task-list')