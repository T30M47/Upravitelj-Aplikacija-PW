import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factory import (
    StudentFactory,
    AplikacijaFactory
)

NUM_STUDENTS=20
NUM_APPS=20

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Student, Aplikacija]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        
        studenti=[]
    
        for _ in range(NUM_STUDENTS):
            student=StudentFactory()
            studenti.append(student)
 
        for _ in range(NUM_APPS):
            aplikacija=AplikacijaFactory()
            moguci=[1,2,3]
            odabir=random.choice(moguci)
            aplikacija_studenti=random.choices(studenti, k=odabir)
            aplikacija.aplikacija_student.add(*aplikacija_studenti)
