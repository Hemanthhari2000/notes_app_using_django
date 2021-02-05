from django.apps import AppConfig


class AppNoteConfig(AppConfig):
    name = 'app_note'

    def ready(self):
        import app_note.signals
