from django.apps import AppConfig

class DigiatServicesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'digiat_services_app'

    def ready(self):
        import digiat_services_app.signals  # save signal to be intiated automatically while app start