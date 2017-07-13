from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """
    Executes all of Janeway's cron tasks.
    """

    help = "Executes all of Janeway's cron tasks."

    def handle(self, *args, **options):
        """Executes all of Janeway's cron tasks.

        :param args: None
        :param options: None
        :return: None
        """
        print("Executing cron tasks now.")
        call_command('send_reminders')