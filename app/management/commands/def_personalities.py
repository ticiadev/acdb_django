from django.core.management.base import BaseCommand, CommandError
from app.models import Personality


class Command(BaseCommand):

    def handle(self, *args, **options):
        normal = Personality(type='normal', gender='female')
        peppy = Personality(type='peppy', gender='female')
        snooty = Personality(type='snooty', gender='female')
        uchi = Personality(type='uchi', gender='female')
        lazy = Personality(type='lazy', gender='male')
        jock = Personality(type='jock', gender='male')
        smug = Personality(type='smug', gender='male')
        cranky = Personality(type='cranky', gender='male')

        personalities = [normal, peppy, snooty, uchi, lazy, jock, smug, cranky]
        for p in personalities:
            p.save()
