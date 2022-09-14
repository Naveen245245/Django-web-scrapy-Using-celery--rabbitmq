from django.urls import path,include
from . views import index,createApp,appDetailView,submitTask,userTasks,userPoints,loginView,logoutView
urlpatterns = [

    path('login/',loginView,name="login"),
    path('logout/',logoutView,name="logout"),
    path('index/',index,name="index"),
    path('create/',createApp,name="create-app"),
    path('<int:pk>/',appDetailView,name="app-details"),
    path('submit/<int:pk>/',submitTask,name="submit-task"),
    path('tasks/<int:pk>/',userTasks,name="tasks"),
    path('points/<int:pk>/',userPoints,name="points"),

    

    
]

