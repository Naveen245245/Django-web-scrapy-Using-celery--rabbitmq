from django.contrib import admin

# Register your models here.
from . models import App,UserProfile,Tasks

class AppAdmin(admin.ModelAdmin):
    list_display = ['id','app_name','app_link','category','sub_Category','score','logo']

admin.site.register(App,AppAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','points']

admin.site.register(UserProfile,UserProfileAdmin)

class TasksAdmin(admin.ModelAdmin):
    list_display = ['id','user','app','screenshot','taskComplete']

admin.site.register(Tasks,TasksAdmin)