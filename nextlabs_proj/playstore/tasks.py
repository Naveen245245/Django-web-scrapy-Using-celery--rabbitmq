from __future__ import absolute_import,unicode_literals
from celery import shared_task
import logging

from google_play_scraper import app



@shared_task
def add(x,y):
    return x+y



@shared_task
def scrapeApp(app_link):
    result = app(
        app_link,
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )
    appdata = []
    appdata.append(result['genre'])
    appdata.append(result['summary'])
    appdata.append(result['icon'])
    logging.info("Result type {} and genre{}".format(type(result),result['genre']))
    return appdata
# @shared_task
# def scrapeApp(app_instance):
#     logging.info("Instance details {} and type {}".format(app_instance,type(app_instance)))
#     # app_link_get = app_instance['fields'].get(app_link)
#     # logging.info("Testing __getitem__{}".format(app_link_get))
#     app_link = app_instance['fields']['app_link']
#     app_data_str= app_instance[0]
#     logging.info("String indexfor appindex{}".format(app_data_str))
#     logging.info("App name {} App link {} ".format(app_instance.app_name, app_link))
#     result = app(
#         app_link,
#         lang='en', # defaults to 'en'
#         country='us' # defaults to 'us'
#     )
#     logging.info("Result type {} and genre{}".format(type(result),result['genre']))
#     app_instance['fields']['category'] = result['genre']
#     app_instance['fields']['sub_Category'] = result['genreId']
#     app_instance['fields']['logo'] = result['icon']
#     app_instance['fields']['score'] = round(result['score']*100,2)
#     # app_instance.save()
#     # app_instance.category = result['genre']
#     # app_instance.sub_Category = result['genreId']
#     # app_instance.logo = result['icon']
#     # app_instance.score = round(result['score']*100,2)
#     # app_instance.save()
#     # logging.info("App category {} sub_Category {} score {} logo {}".format(app_instance.category, app_instance.sub_Category,app_instance.score,app_instance.logo))
#     logging.info("App category {} sub_Category {} score {} logo {}".format(app_instance['fields']['category'],
#                                                  app_instance['fields']['sub_Category'],
#                                                  app_instance['fields']['score'],
#                                                  app_instance['fields']['logo']))
#     return app_instance





