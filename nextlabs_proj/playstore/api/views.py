from rest_framework import viewsets
from playstore.models import Tasks,App
from playstore.tasks import scrapeApp
from . seriailizers import TasksSerializers,AppSerializer
from django.http.response import JsonResponse
from rest_framework import status

import logging 

class TasksViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `CRUD` actions.
    """
    queryset = Tasks.taskManager.all()
    serializer_class = TasksSerializers


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.appManager.all()
    serializer_class = AppSerializer

    def create(self, request):
        logging.info("Fetching  form is through get")
        if request.method == "POST":
            app_link = request.POST.get("app_link")
            logging.info("Calling celery scrapeApp with app link {}",app_link)
            app_data = scrapeApp(app_link)
            logging.info("App category {} summary {} logo {}".format(app_data[0], app_data[1],app_data[2]))
            post_data = request.POST.copy()
            logging.info("Post data {}".format(post_data))
            post_data.update({"category":app_data[0],"sub_Category":app_data[1],"logo":app_data[2]})
            
            logging.info("Post data {}".format(post_data))
            appSerializer = AppSerializer(data = post_data)
            logging.info("Fetching  form is through post")
            
            if appSerializer.is_valid():
                logging.info("Checking form inside valid ")
                appSerializer.save() 
                return JsonResponse(appSerializer.data, status=status.HTTP_201_CREATED) 
        

        return JsonResponse(appSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
