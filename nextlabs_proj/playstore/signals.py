# from django.db.models.signals import post_save,pre_save
# from django.core import serializers

# from . api.seriailizers import AppSerializer

# import logging

# from . tasks import scrapeApp
# from . models import App

# def update_apps(sender, instance, **kwargs):
#     if(instance.category=="" or instance.sub_Category=="",instance.logo==""):
#         logging.info("Calling celery scrapeApp")
#         app_data = scrapeApp(instance.app_name,instance.app_link)
#         logging.info("App genere {} summary {} icon {}".format(app_data[0],app_data[2],app_data[1]))

#         app_obj = App.objects.get(id=instance.id)
#         logging.info("App object {}".format(app_obj))
#         app_obj.category = app_data[0]
#         app_obj.sub_Category = app_data[2]
#         app_obj.logo = app_data[1]
#         app_obj.save()
#         logging.info("App object saved successfully")
#         # instance.category = app_data[0]
#         # instance.sub_Category = app_data[2]
#         # instance.logo = app_data[1]
#         # instance.save()
#         # instance.save(update_fields=['category', 'sub_Category','logo'])
#         # logging.info("App data fetched and saved")

#     # obj.save()


# # def update_apps(sender, instance, created, **kwargs):
# #     logging.info("Calling celery scrapeApp")
# #     scrapeApp(instance)
#     # obj.save()


# # def update_apps(sender, instance, created, **kwargs):
# #     logging.info("Calling celery scrapeApp")
# #     serialized_obj = serializers.serialize('json', [instance])
    
# #     serialized_objupdated = scrapeApp.delay(instance)
# #     # serialized_objupdated = scrapeApp.delay(serialized_obj)

# #     obj = next(serializers.deserialize("json", serialized_objupdated)).object

# #     logging.info("App data scraped and saved completed {}",obj)
# #     obj.save()


# # post_save.connect(update_apps, sender=App)
# pre_save.connect(update_apps, sender=App)




