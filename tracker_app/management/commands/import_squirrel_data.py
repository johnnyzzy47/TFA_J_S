from django.core.management import BaseCommand

class Command(BaseCommand):
        help = 'Load squirrel data  into the database'

        def add_arguments(self,parser):
            parser.add_argument('path', type=str, help = 'file containing data')

        def handle(self, *args, **kwargs):
            path = kwargs['path']
            msg = f'You are importing from {file_}'
            self.stdout.write(self.style.SUCCESS(msg))
