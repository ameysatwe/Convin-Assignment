from django.urls import include,path
from Scheduler import views

urlpatterns=[
    path('getTasks',views.get_Tasks),
    path('createTasks',views.create_Tasks),
    path('updateTask/<int:task_id>',views.update_Tasks),
    path('getTaskTracker',views.getTaskTrackers.as_view())
]