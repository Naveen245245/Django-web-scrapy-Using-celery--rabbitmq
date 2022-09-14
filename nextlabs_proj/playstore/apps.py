from django.apps import AppConfig


class PlaystoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playstore'

    def ready(self):
        import playstore.signals