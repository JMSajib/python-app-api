import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Django command to pause execution until database is available"""
        self.stdout.write('Waiting for Databse...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavilable,waiting for 1 sec...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database avilable!!'))
