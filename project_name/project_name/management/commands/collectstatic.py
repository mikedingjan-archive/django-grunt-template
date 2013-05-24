import os

from django.conf import settings
from django.contrib.staticfiles.management.commands.collectstatic import Command as CollectstaticCommand


class Command(CollectstaticCommand):
    """
    Make sure the media dir exists before we're running collecstatic.
    """
    def inner_run(self, *args, **options):
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)
        super(Command, self).inner_run(*args, **options)


