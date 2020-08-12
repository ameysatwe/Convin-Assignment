from django.urls import include,path
from Scheduler.views import router
#from Scheduler import views
urlpatterns=[
    path('',include(router.urls)),
    #path('index',views.index)
]