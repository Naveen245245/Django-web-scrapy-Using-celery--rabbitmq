from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

import logging

from . models import App,UserProfile,Tasks
from .forms import AppForm
from.tasks import scrapeApp


def loginView(request):
    # if request.user.is_authenticated:
    #     return redirect('index')
    context={
            "loginform":AuthenticationForm
        }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, '{} was Successful logged in !'.format(username))
            return redirect("index")
        else:
            messages.error(request, 'Username or password is incorrect')
            return render(request, 'playstore/login.html',context)
    return render(request, 'playstore/login.html',context)
        
def logoutView(request):
    logout(request)
    messages.info(request, 'User was logout !')
    return redirect('login')

def index(request):
    apps = App.appManager.all()
    userProfiles = UserProfile.objects.all()
    user = request.user
    context = {
        "apps": apps,
        "user":user
    }
    logging.info("All apps:{} user {}".format(apps,user))
    return render(request,'playstore/index.html',context)



def createApp(request):
    logging.info("Fetching  form is through get")
    if request.method == "POST":
        # app_link = appForm.cleaned_data.get("app_link")
        app_link = request.POST.get("app_link")
        logging.info("Calling celery scrapeApp with app link {}",app_link)
        app_data = scrapeApp(app_link)
        logging.info("App category {} summary {} logo {}".format(app_data[0], app_data[1],app_data[2]))
        post_data = request.POST.copy()
        logging.info("Post data {}".format(post_data))
        post_data.update({"category":app_data[0],"sub_Category":app_data[1],"logo":app_data[2]})
        
        logging.info("Post data {}".format(post_data))
        # appForm = AppForm(request.POST)
        appForm = AppForm(post_data)
        
        logging.info("Fetching  form is through post")
        
        if appForm.is_valid():
            logging.info("Checking form inside valid ")
            appForm.save() 
            messages.success(request, 'User was Successful logged in !')
            return redirect("index")
    appForm = AppForm()

    return render(request, "playstore/createApp.html", {"appForm": appForm})


def appDetailView(request,pk):
    app = App.appManager.get(id=pk)
    # logging("App details {}".format(app.app_name))
    context={
        "app":app
    }
    return render(request, "playstore/appdetails.html", context)

def submitTask(request,pk):
    # print(request.FILES)
    app=App.appManager.get(id=pk)
    if(request.method=='POST'):
        screenshot_file = request.FILES.get('file')
        Tasks.taskManager.create(screenshot=screenshot_file,user= request.user,app=app)
    return HttpResponse('Uploaded..')

def userTasks(request,pk):
    user = request.user
    # tasks_completed = Tasks.objects.filter(user=user,taskComplete=True)
    apps=[]
    tasks_completed = Tasks.taskManager.get_user_completed(user)
    for task in tasks_completed:
        apps.append(task.app.id)
        
    tasks_submitted = Tasks.taskManager.get_user_submitted(user)
    for task in tasks_submitted:
        apps.append(task.app.id)

    
    tasks_pending = App.appManager.user_pending_apps(apps)
    context={
        "tasks_completed":tasks_completed,
        "tasks_submitted":tasks_submitted,
        "tasks_pending":tasks_pending
    }
    return render(request, 'playstore/tasks.html',context)

def userPoints(request,pk):
    user = request.user
    user_score = Tasks.taskManager.get_user_score(user)
    context={
        "user":user,
        "user_score":user_score
    }
    return render(request, 'playstore/points.html',context)