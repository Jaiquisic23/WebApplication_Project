from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'
    default_app_config = 'store.apps.StoreConfig'

    def ready(self):
        import store.signals