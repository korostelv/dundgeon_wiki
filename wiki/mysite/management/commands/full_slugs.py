from django.core.management.base import BaseCommand
from django.utils.text import slugify
from mysite.models import Release

class Command(BaseCommand):
    help = 'Добавить слаги выпускам'

    def handle(self, *args, **kwargs):
        for release in Release.objects.all():
            if not release.slug:
                release.slug = slugify(release.title)
                release.save()
                self.stdout.write(self.style.SUCCESS(f'Slug добавлен для выпуска: {release.title}'))