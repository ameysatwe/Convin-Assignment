from django.urls import include,path
from Scheduler.views import router

urlpatterns=[
    path('',include(router.urls))
]