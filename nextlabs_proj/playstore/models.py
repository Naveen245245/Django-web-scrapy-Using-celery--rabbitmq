from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AppManager(models.Manager):
    def user_pending_apps(self,apps):
        return super().get_queryset().exclude(id__in=apps)
        
class App(models.Model):
    app_name = models.CharField(max_length=50)
    app_link = models.CharField(max_length=50)
    category = models.CharField(max_length=30,blank=True)
    sub_Category = models.CharField(max_length=200,blank=True)
    score = models.IntegerField(default=0)
    logo = models.CharField(max_length=300,blank=True)

    appManager = AppManager()

    def __str__(self):
        return self.app_name

    class Meta:
        ordering = ['-id']

    
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    points = models.IntegerField(default=0)

    


class TaskManager(models.Manager):
    def get_user_completed(self,pk):
        return super().get_queryset().filter(user=pk,taskComplete=True)

    def get_user_submitted(self,pk):
        return super().get_queryset().filter(user=pk,taskComplete=False)

    def get_user_score(self,pk):
        user_score = 0
        tasks = super().get_queryset().filter(user=pk,taskComplete=True)
        for task in tasks:
            user_score += task.app.score
        return user_score


    


class Tasks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='images/',blank=True)
    taskComplete = models.BooleanField(default=False)

    taskManager = TaskManager()