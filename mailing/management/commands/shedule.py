from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management import BaseCommand
from mailing.sendmailing import send_mailing


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler()
        scheduler.add_job(
            send_mailing,
            trigger=CronTrigger(second="*/10"),
            id="sendmail",
            max_instances=10,
            replace_existing=True,
        )

        try:
            print("Start scheduler")
            scheduler.start()

        except KeyboardInterrupt:
            print("Stop scheduler")
            scheduler.shutdown()
            print("Exit")
