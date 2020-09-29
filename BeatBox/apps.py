from django.apps import AppConfig


class BeatboxConfig(AppConfig):
    name = 'BeatBox'

    def ready(self):
        import BeatBox.signals