from django.apps import AppConfig


class PluginApiConfig(AppConfig):
    name = 'plugin_api'

    def ready(self):
        from p1.models import machine
