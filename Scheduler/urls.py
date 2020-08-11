from django.urls import include,path
from Scheduler import views

urlpatterns=[
    path('getTasks',views.get_Tasks),
    path('createTasks',views.create_Tasks),
    path('getTask/<int:id>',views.get_One),
    path('updateTask/<int:task_id>',views.update_Tasks),
    path('tracker',views.getTaskTrackers.as_view())
    # path('getTaskTracker',views.getTaskTrackers.as_view()),
    # path('taskDeets',views.TaskList.as_view(),name='task-list'),
    # path('put',views.TaskDetail.as_view(),name='task-detail')
]