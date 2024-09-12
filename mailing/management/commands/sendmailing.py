from django.core.management import BaseCommand
from mailing.sendmailing import shedule


class Command(BaseCommand):
    """Кастомная команда для рассылки данных по почте"""

    def handle(self, *args, **options):
        """Соответственно метод для рассылки данных по почте"""
        shedule()
