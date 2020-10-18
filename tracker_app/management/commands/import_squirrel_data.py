import csv

from django.core.management import BaseCommand
from tracker_app.models import Squirrel
import argparse

from distutils.util import strtobool

class Command(BaseCommand):
        help = 'Load squirrel data into the database'

        def add_arguments(self,parser):
            parser.add_argument('path', type=str, help = 'file containing data')

        def handle(self, *args, **kwargs):
            Squirrel.objects.all().delete()
            path = kwargs['path']
            msg = f'You are importing'
            self.stdout.write(self.style.SUCCESS(msg))
