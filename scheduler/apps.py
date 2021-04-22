from django.apps import AppConfig
from django.conf import settings

class SchedulerConfig(AppConfig):
    name = 'scheduler'

    def ready(self):
        from . import scheduler
        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()