from django.core.management.base import BaseCommand
from app.models import Game
import itertools


class Command(BaseCommand):

    def handle(self, *args, **options):
        ac = Game(name='Animal Crossing', console='Gamecube',
                  year_released=2002)
        ww = Game(name='Wild World', console='DS', year_released=2005)
        cf = Game(name='City Folk', console='Wii', year_released=2008)
        nl = Game(name='New Leaf', console='3DS', year_released=2012)
        nh = Game(name='New Horizons', console='Switch', year_released=2020)

        games = [ac, ww, cf, nl, nh]
        for g in games:
            g.save()