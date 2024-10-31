from django.apps import AppConfig





class GanaderiaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ganaderia'

    def ready(self):

        pass
        # Asegúrate de que la importación de señales esté aquí
        import ganaderia.signals
