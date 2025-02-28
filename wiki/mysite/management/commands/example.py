from django.core.management.base import BaseCommand

from mysite.models import Race


class Command(BaseCommand):
    help = 'Посмотреть список рас'

    def handle(self, *args, **kwargs):
        for race in Race.objects.all():
            print(race.name)

