from django.core.management.base import BaseCommand
from app.models import Coffee
import itertools


class Command(BaseCommand):

    def handle(self, *args, **options):
        combo = [['Blue Mtn', 'Kilimanjaro', 'Mocha', 'Blend'],
                 [0, 1, 2, 3],
                 [0, 1, 2, 3]]
        blends = list(itertools.product(*combo))
        coffees = []
        for b in blends:
            c = Coffee(beans=b[0], milk=b[1], sugar=b[2])
            coffees.append(c)

        for c in coffees:
            c.save()
