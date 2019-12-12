import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.csv_t()

    @staticmethod
    def csv_t():
        all=[]
        f = csv.reader(open(r'E:\alyun_python_obj\test_obj\static\export_urls.csv', 'r'))
        for i in f:
            print(i[1][51:])
            print(i[1][68:])
            # print(len('meifang/bgmusic2/'))
            pass