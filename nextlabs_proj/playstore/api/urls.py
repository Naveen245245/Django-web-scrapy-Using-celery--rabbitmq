from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import TasksViewSet,AppViewSet
# import views
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tasks', TasksViewSet,basename="task")
router.register(r'apps', AppViewSet,basename="app")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]