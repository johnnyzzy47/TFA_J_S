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
            with open(path, 'rt') as f:
                reader = csv.DictReader(f)
                data = list(reader)
                for row in data:
                    squirrel = Squirrel(
                            X=row['\ufeffX'],
                            Y=row['Y'],
                            UID=row['Unique Squirrel ID'],
                            Shift=row['Shift'],
                            Date=row['Date'],
                            Age=row['Age'],
                            Primary_Fur_Color=row['Primary Fur Color'],
                            Location=row['Location'],
                            Specific_Location=row['Specific Location'],
                            Running=strtobool(row['Running']),
                            Chasing=strtobool(row['Chasing']),
                            Climbing=strtobool(row['Climbing']),
                            Eating=strtobool(row['Eating']),
                            Foraging=strtobool(row['Foraging']),
                            Other_activities=row['Other Activities'],
                            Kuks=strtobool(row['Kuks']),
                            Quaas=strtobool(row['Quaas']),
                            Moans=strtobool(row['Moans']),
                            Tail_flags=strtobool(row['Tail flags']),
                            Tail_twitches=strtobool(row['Tail twitches']),
                            Approaches=strtobool(row['Approaches']),
                            Indifferent=strtobool(row['Indifferent']),
                            Runs_From=strtobool(row['Runs from']),
                            )
                        squirrel.save()
