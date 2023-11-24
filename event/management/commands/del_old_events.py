import datetime

from django.core.management import BaseCommand
from event.models import Event


class Command(BaseCommand):
    help = 'Delete old Events'

    def handle(self, *args, **options):

        try:
            count = 0
            events = Event.objects.filter(date__lt=datetime.date.today())
            for event in events:
                event.delete()
                count += 1
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted Events (count: {count}).'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
